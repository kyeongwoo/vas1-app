import streamlit as st
from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# JSON 인증 파일 경로
json_path = "C:/Users/Administ/OneDrive/바탕 화면/streamlit-form-project-bb6c5ed1ba16.json"

# 구글 시트 인증
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
gc = gspread.authorize(credentials)

# 구글 시트 열기
sheet = gc.open("VAS심리기록").sheet1

# ✅ 모바일에 적합한 페이지 설정
st.set_page_config(page_title="심리 상태 평가", layout="centered")

st.markdown("### 🧠 오늘의 심리 상태를 평가해주세요")
st.markdown(f"#### 📅 오늘 날짜: `{date.today()}`")

# ✅ 이름 + 호흡번호 입력 (세로 배치)
name = st.text_input("👤 이름을 입력해주세요", key="name")
session = st.radio("🔢 호흡 번호를 선택해주세요", options=["1", "2", "3", "4"], key="session", horizontal=True)

st.markdown("---")

# ✅ 슬라이더 4개: 2개씩 2줄로 배치
col1, col2 = st.columns(2)
with col1:
    stress = st.slider("😣 1.스트레스를 얼마나 느끼시나요?", 0, 100, 50)
    fatigue = st.slider("🥱 2. 얼마나 피곤한가요?", 0, 100, 50)
with col2:
    confidence = st.slider("💪 3.자신감은 어느 정도 인가요?", 0, 100, 50)
    anxiety = st.slider("😟 4.불안감을 얼마나 느끼시나요?", 0, 100, 50)

st.markdown("---")

# ✅ 저장 버튼 및 피드백
if st.button("💾 결과 저장"):
    if name:
        sheet.append_row([str(date.today()), name, session, stress, confidence, fatigue, anxiety])
        st.success("✅ 데이터가 저장되었어요! 감사합니다 😊")
    else:
        st.warning("⚠️ 이름을 입력해주세요")
