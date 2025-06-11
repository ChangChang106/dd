import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

# 페이지 설정
st.set_page_config(page_title="🍱 일본 음식 여행 지도", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #d94f4f;'>🍣 일본 음식 여행 가이드</h1>
    <p style='text-align: center;'>맛집은 곧 목적지! 도시별 대표 음식을 지도와 함께 즐기세요.</p>
""", unsafe_allow_html=True)

# --------------------------
# 도시/음식점 데이터 정의
cities = {
    "도쿄": {
        "설명": "도쿄는 전 세계 미식가들이 모이는 도시입니다. 고급 스시집부터 캐주얼 라멘집까지 다양하게 즐길 수 있어요.",
        "음식점": [
            {
                "이름": "스시 사이토",
                "위치": [35.6655, 139.7293],
                "설명": "세계 미쉐린 3스타! 예약이 어려운 전설적인 스시집.",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Sushi_platter.jpg/640px-Sushi_platter.jpg"
            },
            {
                "이름": "이치란 라멘",
                "위치": [35.6595, 139.7005],
                "설명": "혼자 먹기 좋은 1인 좌석! 진한 돈코츠 국물의 라멘 체인.",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Ippudo_Ramen.jpg/640px-Ippudo_Ramen.jpg"
            }
        ]
    },
    "오사카": {
        "설명": "오사카는 일본의 '먹방 도시'. 서민적인 분위기 속에서 다양한 길거리 음식과 전통 요리를 맛볼 수 있어요.",
        "음식점": [
            {
                "이름": "쥬하치반 타코야키",
                "위치": [34.6695, 135.5015],
                "설명": "겉바속촉 타코야키! 오사카 난바 대표 맛집.",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Takoyaki_001.jpg/640px-Takoyaki_001.jpg"
            },
            {
                "이름": "치보 오코노미야키",
                "위치": [34.6689, 135.5023],
                "설명": "일본식 부침개의 끝판왕, 정통 오코노미야키 체험!",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Okonomiyaki_001.jpg/640px-Okonomiyaki_001.jpg"
            }
        ]
    }
}

# --------------------------
# 사이드바 - 도시 선택
selected_city = st.sidebar.selectbox("📍 도시 선택", list(cities.keys()))
city_info = cities[selected_city]

# --------------------------
# 지도 출력
st.subheader(f"🗾 {selected_city} 음식 지도")
map_center = city_info["음식점"][0]["위치"]
m = folium.Map(location=map_center, zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)

for r in city_info["음식점"]:
    popup = f"""
    <b>{r['이름']}</b><br>
    {r['설명']}<br>
    <img src="{r['이미지']}" width="200">
    """
    folium.Marker(
        location=r["위치"],
        popup=popup,
        tooltip=r["이름"],
        icon=folium.Icon(color='red', icon='cutlery', prefix='fa')
    ).add_to(marker_cluster)

st_folium(m, width=1000, height=500)

# --------------------------
# 설명 섹션
st.markdown(f"""
### 🍜 {selected_city}에서 먹어야 할 음식들
{city_info['설명']}
""")

# --------------------------
# 음식점 카드 스타일 출력
st.markdown("### 🍽 음식점 추천")

cols = st.columns(2)
for idx, r in enumerate(city_info["음식점"]):
    with cols[idx % 2]:
        st.image(r["이미지"], use_column_width=True, caption=f"📍 {r['이름']}")
        st.markdown(f"**{r['설명']}**")
        st.markdown("---")
