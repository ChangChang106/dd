import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

# 페이지 설정
st.set_page_config(page_title="🍱 일본 음식 여행 가이드", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #d94f4f;'>🍣 일본 음식 여행 가이드</h1>
    <p style='text-align: center;'>도시별 대표 음식과 맛집을 지도와 이미지로 즐기세요!</p>
""", unsafe_allow_html=True)

# ------------------------
# 도시 및 음식점 데이터 정의
cities = {
    "도쿄": {
        "설명": "도쿄는 전 세계 미식가들이 모이는 도시입니다.",
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
                "설명": "혼자 먹기 좋은 1인 좌석! 진한 돈코츠 국물.",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Ippudo_Ramen.jpg/640px-Ippudo_Ramen.jpg"
            }
        ]
    },
    "오사카": {
        "설명": "오사카는 일본의 '먹방 도시'입니다.",
        "음식점": [
            {
                "이름": "쥬하치반 타코야키",
                "위치": [34.6695, 135.5015],
                "설명": "겉바속촉 타코야키! 난바 대표 맛집.",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Takoyaki_001.jpg/640px-Takoyaki_001.jpg"
            },
            {
                "이름": "치보 오코노미야키",
                "위치": [34.6689, 135.5023],
                "설명": "정통 오코노미야키 체험!",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Okonomiyaki_001.jpg/640px-Okonomiyaki_001.jpg"
            }
        ]
    },
    "삿포로 (홋카이도)": {
        "설명": "삿포로는 진한 미소라멘과 해산물 덮밥이 유명합니다.",
        "음식점": [
            {
                "이름": "스미레 라멘",
                "위치": [43.0567, 141.3407],
                "설명": "삿포로 미소라멘의 정석!",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Miso_ramen.jpg/640px-Miso_ramen.jpg"
            },
            {
                "이름": "중앙시장 카이센동",
                "위치": [43.0639, 141.3543],
                "설명": "알록달록 해물덮밥 전문.",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Kaisendon_by_ystfn.jpg/640px-Kaisendon_by_ystfn.jpg"
            }
        ]
    },
    "후쿠오카": {
        "설명": "후쿠오카는 돈코츠 라멘과 야타이 문화의 본고장.",
        "음식점": [
            {
                "이름": "이치란 본점",
                "위치": [33.5892, 130.4207],
                "설명": "돈코츠 라멘의 원조, 본점.",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Tonkotsu_ramen_by_stu_spivack.jpg/640px-Tonkotsu_ramen_by_stu_spivack.jpg"
            },
            {
                "이름": "텐진 야타이 거리",
                "위치": [33.5904, 130.4017],
                "설명": "밤에만 열리는 포장마차 거리!",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Yatai_Stalls_in_Tenjin.jpg/640px-Yatai_Stalls_in_Tenjin.jpg"
            }
        ]
    },
    "나가사키": {
        "설명": "나가사키는 다양한 문화가 융합된 나가사키 짬뽕과 카스테라가 유명합니다.",
        "음식점": [
            {
                "이름": "시카이로",
                "위치": [32.7413, 129.8776],
                "설명": "나가사키 짬뽕의 발상지!",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Nagasaki_Chanpon.jpg/640px-Nagasaki_Chanpon.jpg"
            }
        ]
    },
    "유자와 (설국)": {
        "설명": "가와바타 야스나리의 『설국』 배경지로, 눈 내리는 온천 마을과 함께 일본 전통의 정취를 느낄 수 있습니다.",
        "음식점": [
            {
                "이름": "에치고유자와역 에키벤",
                "위치": [36.9365, 138.8122],
                "설명": "눈 내리는 역에서 먹는 따뜻한 도시락.",
                "이미지": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Ekiben_Yuzawa.jpg/640px-Ekiben_Yuzawa.jpg"
            }
        ]
    }
}

# 좋아요 초기화
for city in cities.values():
    for r in city["음식점"]:
        if f"like_{r['이름']}" not in st.session_state:
            st.session_state[f"like_{r['이름']}"] = 0

# -----------------------
# 도시 선택
selected_city = st.sidebar.selectbox("📍 도시 선택", list(cities.keys()))
city_info = cities[selected_city]

# 지도 표시
st.subheader(f"🗾 {selected_city} 음식 지도")
map_center = city_info["음식점"][0]["위치"]
m = folium.Map(location=map_center, zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)

for r in city_info["음식점"]:
    popup_html = f"""
        <div style="width:200px">
            <h4>{r['이름']}</h4>
            <img src="{r['이미지']}" style="width:100%; border-radius:10px;"><br>
            <p style="font-size:14px;">{r['설명']}</p>
        </div>
    """
    folium.Marker(
        location=r["위치"],
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=r["이름"],
        icon=folium.Icon(color='red', icon='cutlery', prefix='fa')
    ).add_to(marker_cluster)

st_folium(m, width=1000, height=500)

# 도시 설명
st.markdown(f"""
### 🍜 {selected_city}에서 꼭 먹어야 할 음식들
{city_info['설명']}
""")

# 음식점 카드 + 좋아요
st.markdown("### 🍽 음식점 추천")
cols = st.columns(2)
for idx, r in enumerate(city_info["음식점"]):
    with cols[idx % 2]:
        st.image(r["이미지"], use_column_width=True, caption=f"📍 {r['이름']}")
        st.markdown(f"**{r['설명']}**")
        if st.button(f"❤️ 좋아요 {st.session_state[f'like_{r['이름']}']}", key=r['이름']):
            st.session_state[f"like_{r['이름']}"] += 1
        st.markdown("---")
