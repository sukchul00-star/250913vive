import streamlit as st
import random

st.set_page_config(page_title="오늘의 기분 퀴즈", page_icon="🎉")

st.title("🎉 오늘의 기분 퀴즈")

# 기분 선택
mood = st.radio(
    "오늘 기분은 어떤가요?",
    ["😀 행복해요", "😐 그냥 그래요", "😡 화나요"],
    key="mood_choice"
)

# 상태 초기화
if "mood_submitted" not in st.session_state:
    st.session_state.mood_submitted = False

# 기분 제출 버튼
if st.button("제출하기"):
    st.session_state.mood_submitted = True

# 기분별 멘트
mood_messages = {
    "😀 행복해요": "기분이 좋아 보이네요! 🎶 오늘 하루도 즐겁게 보내요!",
    "😐 그냥 그래요": "조금 지루할 수도 있지만, 작은 웃음이 힘이 될 거예요 😊",
    "😡 화나요": "화가 날 때는 웃음이 좋은 약이에요. 함께 풀어볼까요? 🤗"
}

# 기분별 퀴즈 데이터
quizzes = {
    "😀 행복해요": [
        {
            "question": "😀 웃으면 길어지는 것은?",
            "options":
