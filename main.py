import streamlit as st
import random

st.set_page_config(page_title="오늘의 기분 퀴즈", page_icon="🎉")

st.title("🎉 오늘의 기분 퀴즈")

# 기분 선택
mood = st.radio(
    "오늘 기분은 어떤가요?",
    ["😀 행복해요", "😐 그냥 그래요", "😡 화나요"]
)

# 기분별 멘트
mood_messages = {
    "😀 행복해요": "기분이 좋아 보이네요! 🎶 오늘 하루도 즐겁게 보내요!",
    "😐 그냥 그래요": "조금 지루할 수도 있지만, 작은 웃음이 힘이 될 거예요 😊",
    "😡 화나요": "화가 날 때는 웃음이 좋은 약이에요. 함께 풀어볼까요? 🤗"
}

#
