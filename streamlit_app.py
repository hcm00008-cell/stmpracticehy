import streamlit as st

st.title("뚱뚱이네 홈페이지에 방문하신 것을 환영합니다")
st.write(
    "자세한 내용을 보고 싶다면(https://docs.streamlit.io/)."
)
# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

# 이미지 출력
st.image("https://static.streamlit.io/examples/cat.jpg", caption="귀여운 고양이", use_container_width=True)
st.image("https://via.placeholder.com/300", caption="예시 이미지")

# 영상 출력
st.video("https://www.youtube.com/watch?v=4nU-Fp96p8E")
st.video("https://www.youtube.com/watch?v=B1J6Ou4q8vE")

# 오디오 출력
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 지도 출력
import pandas as pd
df = pd.DataFrame({"lat": [37.5], "lon": [127.0]})
st.map(df, zoom=12)

# 데이터프레임 테이블 출력
st.dataframe(pd.DataFrame({
    "이름": ["홍길동", "김철수", "박철수"],
    "점수": [85, 92, 100]
}))

# 범위 내 숫자 슬라이드 선택
level = st.slider("난이도를 선택하세요", 1, 100, 5)
st.write("선택한 난이도:", level)

# 날짜 입력
date = st.date_input("날짜를 선택하세요")
st.write("선택한 날짜:", date)

# 시간 입력
time = st.time_input("시간을 선택하세요")
st.write("선택한 시간:", time)