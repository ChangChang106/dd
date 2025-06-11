import streamlit as st

# Streamlit 설정
st.set_page_config(page_title="한국 문학 작가 소개", layout="wide")
st.title("📚 한국의 문학 작가들")
st.markdown("시대별 대표 작가들과 작품을 소개합니다.")

# 작가 정보
authors = {
    "근대 문학": [
        {
            "name": "이광수",
            "works": ["무정", "흙"],
            "quote": "사랑이란 서로의 아픔을 함께 나누는 것."
        },
        {
            "name": "현진건",
            "works": ["운수 좋은 날", "빈처"],
            "quote": "그날 따라 비가 왔다. 그 비는 그의 눈물과 같았다."
        },
        {
            "name": "김동인",
            "works": ["감자", "붉은 산"],
            "quote": "그 여인의 눈 속에는 삶보다 더 짙은 굶주림이 있었다."
        },
        {
            "name": "나도향",
            "works": ["벙어리 삼룡이", "물레방아"],
            "quote": "사랑이란 그리움 속에서도 목마름이었다."
        },
        {
            "name": "염상섭",
            "works": ["만세전", "삼대"],
            "quote": "이 나라는 지금 어디로 가고 있는가."
        },
    ],
    "현대 문학": [
        {
            "name": "한강",
            "works": ["채식주의자", "소년이 온다"],
            "quote": "나는 사라지고 싶었다. 아주 작고 투명한 존재가 되어."
        },
        {
            "name": "공지영",
            "works": ["우리들의 행복한 시간", "도가니"],
            "quote": "용서란, 과거의 고통을 안고 미래로 나아가는 일이다."
        },
        {
            "name": "김영하",
            "works": ["살인자의 기억법", "검은 꽃"],
            "quote": "인간은 망각을 통해 견디는 동물이다."
        },
        {
            "name": "정유정",
            "works": ["7년의 밤", "종의 기원"],
            "quote": "괴물은 태어나는 것이 아니라 만들어지는 것이다."
        },
        {
            "name": "김훈",
            "works": ["칼의 노래", "남한산성"],
            "quote": "칼은 말이 없었다. 그러나 그의 침묵은 역사를 말했다."
        },
    ]
}

# UI 출력
for era, authors_list in authors.items():
    st.header(f"📖 {era}")
    for author in authors_list:
        st.subheader(author["name"])
        st.markdown(f"**대표작:** {', '.join(author['works'])}")
        st.markdown(f"> *{author['quote']}*")
        st.markdown("---")
