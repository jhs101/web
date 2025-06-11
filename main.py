import streamlit as st
import folium
from streamlit_folium import st_folium

# Streamlit 설정
st.set_page_config(page_title="스페인 여행 가이드", layout="wide")
st.title("🇪🇸 스페인 여행 가이드")
st.subheader("지도와 함께 스페인의 주요 여행지를 알아보세요!")

# 도시 정보 데이터
destinations = {
    "바르셀로나": {
        "설명": "지중해의 매력을 지닌 바르셀로나는 가우디의 건축물과 해변이 유명해요.",
        "명소": [
            "사그라다 파밀리아 성당",
            "구엘 공원",
            "람블라스 거리",
            "바르셀로네타 해변"
        ],
        "위치": [41.3851, 2.1734]
    },
    "마드리드": {
        "설명": "스페인의 수도 마드리드는 예술과 역사, 쇼핑과 야경을 모두 즐길 수 있는 도시입니다.",
        "명소": [
            "프라도 미술관",
            "왕궁",
            "솔 광장",
            "레티로 공원"
        ],
        "위치": [40.4168, -3.7038]
    },
    "세비야": {
        "설명": "안달루시아 지방의 중심도시 세비야는 플라멩코와 알카사르 궁전으로 유명해요.",
        "명소": [
            "세비야 대성당",
            "히랄다 탑",
            "알카사르",
            "스페인 광장"
        ],
        "위치": [37.3891, -5.9845]
    },
    "그라나다": {
        "설명": "그라나다는 스페인 이슬람 문화의 중심지로, 알람브라 궁전이 매우 유명합니다.",
        "명소": [
            "알람브라 궁전",
            "알바이신 지구",
            "그라나다 대성당"
        ],
        "위치": [37.1773, -3.5986]
    }
}

# 선택 박스
selected_city = st.selectbox("📍 궁금한 도시를 선택하세요:", list(destinations.keys()))

info = destinations[selected_city]

# 지도 생성
st.markdown("### 🗺️ 위치 보기")
map_center = info["위치"]
m = folium.Map(location=map_center, zoom_start=6)

# 도시 위치 마커
for city, data in destinations.items():
    folium.Marker(
        location=data["위치"],
        popup=f"<b>{city}</b><br>{data['설명']}",
        tooltip=city,
        icon=folium.Icon(color="blue" if city != selected_city else "red")
    ).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)

# 도시 설명
st.markdown(f"## 📌 {selected_city}")
st.write(info["설명"])
st.markdown("### 📍 주요 명소:")
for place in info["명소"]:
    st.markdown(f"- {place}")

# 추가 정보
st.markdown("---")
st.info("💡 팁: 지역별 기후를 고려해서 계절별 옷차림을 챙기세요!")

