import streamlit as st
import folium
from streamlit_folium import st_folium

# 타이틀
st.title("🇯🇵 일본 여행지 가이드")
st.markdown("일본의 대표적인 도시들을 쉽고 자세하게 알아보고 지도에서 위치도 확인해보세요!")

# 여행지 데이터
places = {
    "도쿄": {
        "위치": [35.682839, 139.759455],
        "설명": "일본의 수도로, 쇼핑과 먹거리가 풍부한 도시입니다. 도쿄타워, 아사쿠사, 하라주쿠 등이 유명합니다."
    },
    "교토": {
        "위치": [35.011636, 135.768029],
        "설명": "일본의 전통이 살아있는 도시로, 기온, 금각사, 후시미이나리 신사 등으로 유명합니다."
    },
    "오사카": {
        "위치": [34.693738, 135.502165],
        "설명": "유니버설 스튜디오와 도톤보리 거리로 잘 알려져 있으며, 맛집이 많은 도시입니다."
    },
    "삿포로": {
        "위치": [43.066666, 141.350006],
        "설명": "홋카이도의 중심도시로, 겨울 눈축제와 맥주, 라멘이 유명합니다."
    },
    "후쿠오카": {
        "위치": [33.590355, 130.401716],
        "설명": "규슈의 중심도시로, 하카타 라멘과 텐진 지역이 인기입니다."
    }
}

# 선택 상자
selected_place = st.selectbox("방문할 도시를 선택하세요:", list(places.keys()))

# 도시 설명 출력
st.subheader(f"📍 {selected_place}")
st.write(places[selected_place]["설명"])

# 지도 생성
m = folium.Map(location=places[selected_place]["위치"], zoom_start=12)
folium.Marker(
    places[selected_place]["위치"],
    tooltip=selected_place,
    popup=places[selected_place]["설명"]
).add_to(m)

# 지도 표시
st_folium(m, width=700, height=500)

