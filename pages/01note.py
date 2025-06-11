import streamlit as st
import os
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime

# 디렉토리 생성
UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# DB 연결
engine = create_engine("sqlite:///notes.db")
meta = MetaData()

# 테이블 정의
notes_table = Table(
    "notes", meta,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("filename", String),
    Column("note", String),
    Column("timestamp", DateTime)
)

# 테이블 생성
meta.create_all(engine)

# UI 시작
st.title("🧠 문제 오답노트 공유 시스템 (DB 저장)")

uploaded_file = st.file_uploader("📤 문제 파일 업로드", type=["png", "jpg", "jpeg", "pdf", "txt"])
note = st.text_area("📝 오답노트 입력")
username = st.text_input("👤 이름 또는 닉네임")

if st.button("저장하기"):
    if not uploaded_file or not note.strip() or not username.strip():
        st.warning("모든 입력을 완료해 주세요.")
    else:
        # 파일 저장
        timestamp = datetime.now()
        file_ext = os.path.splitext(uploaded_file.name)[-1]
        saved_filename = f"{username}_{timestamp.strftime('%Y%m%d_%H%M%S')}{file_ext}"
        saved_path = os.path.join(UPLOAD_FOLDER, saved_filename)

        with open(saved_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # DB 저장
        with engine.connect() as conn:
            conn.execute(notes_table.insert().values(
                username=username,
                filename=saved_filename,
                note=note,
                timestamp=timestamp
            ))

        st.success("✅ 저장 완료!")

# 공유된 노트 보기
st.subheader("📚 공유된 오답노트 보기")

with engine.connect() as conn:
    result = conn.execute(notes_table.select().order_by(notes_table.c.timestamp.desc()))
    rows = result.fetchall()

if rows:
    for row in rows:
        with st.expander(f"{row.username} - {row.timestamp.strftime('%Y-%m-%d %H:%M')}"):
            file_path = os.path.join(UPLOAD_FOLDER, row.filename)
            if row.filename.lower().endswith((".png", ".jpg", ".jpeg")):
                st.image(file_path)
            elif row.filename.lower().endswith(".pdf"):
                with open(file_path, "rb") as f:
                    st.download_button("📄 PDF 다운로드", f, file_name=row.filename)
            elif row.filename.lower().endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f:
                    st.text(f.read())

            st.markdown(f"**📝 오답노트:** {row.note}")
else:
    st.info("아직 등록된 오답노트가 없습니다.")
