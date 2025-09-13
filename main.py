# streamlit_app.py
import streamlit as st
import random

st.set_page_config(page_title="오늘의 기분 퀴즈", page_icon="🎉")
st.title("🎉 오늘의 기분 퀴즈")

# --- 초기 세션 상태 설정 ---
if "mood_submitted" not in st.session_state:
    st.session_state.mood_submitted = False
if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = None
if "current_quiz" not in st.session_state:
    st.session_state.current_quiz = None
if "answer_checked" not in st.session_state:
    st.session_state.answer_checked = False

# --- 퀴즈 데이터 및 멘트 ---
mood_options = ["😀 행복해요", "😐 그냥 그래요", "😡 화나요"]

mood_messages = {
    "😀 행복해요": "기분이 좋아 보이네요! 🎶 오늘 하루도 즐겁게 보내요!",
    "😐 그냥 그래요": "조금 지루할 수도 있지만, 작은 웃음이 힘이 될 거예요 😊",
    "😡 화나요": "화가 날 때는 웃음이 좋은 약이에요. 함께 풀어볼까요? 🤗"
}

quizzes = {
    "😀 행복해요": [
        {"question": "웃으면 길어지는 것은?", "options": ["머리카락", "하루", "팔", "입꼬리"], "answer": "입꼬리"},
        {"question": "토마토가 웃으면 뭐라 할까요?", "options": ["케첩!", "샐러드", "방울토마토", "토마토"], "answer": "케첩!"},
        {"question": "햇님이 학교에 가면 뭐가 될까요?", "options": ["교실등", "학생", "태양빛", "해답"], "answer": "해답"},
    ],
    "😐 그냥 그래요": [
        {"question": "바닷가에서 가장 게으른 동물은?", "options": ["거북이", "게", "조개", "갈매기"], "answer": "조개"},
        {"question": "컴퓨터가 배고프면 먹는 건?", "options": ["칩", "쿠키", "파일", "바이러스"], "answer": "칩"},
        {"question": "항상 바쁜 벌레는?", "options": ["개미", "잠자리", "바퀴벌레", "메뚜기"], "answer": "개미"},
    ],
    "😡 화나요": [
        {"question": "화가
