import streamlit as st

st.title("홈페이지에 방문하신 것을 환영합니다!!!")
st.write(
    "자세한 내용을 보고 싶다면(https://docs.streamlit.io/)."
)
# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다!.")

import streamlit as st
import pandas as pd

st.title("1️⃣ ✅ 공개 Google Sheet 읽기")
st.info("📘 누구나 볼 수 있도록 공개된 시트를 Pandas로 직접 불러오는 가장 간단한 방법입니다.\n📎 링크는 반드시 `export?format=csv` 형태로 설정하세요.")

csv_url1 = st.secrets["connections"]["gsheets"]["public_url"]
df1 = pd.read_csv(csv_url1)
st.subheader("Choice 값 막대그래프!")
choice_counts = df1["choice"].value_counts()
st.bar_chart(choice_counts)

st.subheader("Choice 값 (카운트)")
st.dataframe(choice_counts.rename_axis("choice").reset_index(name="count"))
st.write(st.secrets["openai"]["api_key"])