import streamlit as st
from PIL import Image
import os

def load_image(image_path, placeholder_path="images/placeholder.jpg"):
    try:
        if os.path.exists(image_path):
            return Image.open(image_path)
        else:
            return Image.open(placeholder_path)
    except:
        return Image.open(placeholder_path)

# Streamlit 페이지 설정
st.set_page_config(page_title="한국 문학 작가 소개", layout="wide")
st.title("📚 한국의 문학 작가들")

# (authors 딕셔너리는 이전 답변의 내용 사용)

# 작가 소개
for era, authors_list in authors.items():
    st.header(f"📖 {era}")
    for author in authors_list:
        cols = st.columns([1, 2])
        with cols[0]:
            image = load_image(author["image"])
            st.image(image, caption=author["name"], use_column_width=True)
        with cols[1]:
            st.subheader(author["name"])
            st.markdown(f"**대표작:** {', '.join(author['works'])}")
            st.markdown(f"> *{author['quote']}*")
        st.markdown("---")

