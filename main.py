import streamlit as st
import random

st.set_page_config(page_title="오늘의 기분 퀴즈", page_icon="🎉")

st.title("🎉 오늘의 기분 퀴즈")

# 기분 선택
mood = st.radio(
    "오늘 기분은 어떤가요?",
    ["😀 행복해요", "😐 그냥 그래요", "😡 화나요"]
)

# 기분별 퀴즈 데이터 (여러 개씩 준비)
quizzes = {
    "😀 행복해요": [
        {
            "question": "😀 웃으면 길어지는 것은?",
            "options": ["머리카락", "하루", "팔", "입꼬리"],
            "answer": "입꼬리"
        },
        {
            "question": "😀 햇님이 학교에 가면 뭐가 될까요?",
            "options": ["교실등", "학생", "태양빛", "해답"],
            "answer": "해답"
        },
        {
            "question": "😀 토마토가 웃으면 뭐라고 할까요?",
            "options": ["케첩!", "웃음토마토", "방울토마토", "샐러드"],
            "answer": "케첩!"
        },
    ],
    "😐 그냥 그래요": [
        {
            "question": "😐 항상 바쁜 벌레는?",
            "options": ["개미", "잠자리", "바퀴벌레", "메뚜기"],
            "answer": "개미"
        },
        {
            "question": "😐 바다가 화가 나면 뭐가 될까요?",
            "options": ["태풍", "파도", "바다거품", "소금"],
            "answer": "파도"
        },
        {
            "question": "😐 컴퓨터가 배고프면 먹는 건?",
            "options": ["칩", "쿠키", "파일", "바이러스"],
            "answer": "칩"
        },
    ],
    "😡 화나요": [
        {
            "question": "😡 화난 연필이 하는 말은?",
            "options": ["지우지마!", "꺾지마!", "난 연필심이야!", "써!"],
            "answer": "지우지마!"
        },
        {
            "question": "😡 화가 풀리면 생기는 강은?",
            "options": ["한강", "냉강", "화강", "평강"],
            "answer": "평강"
        },
        {
            "question": "😡 못생긴 감자가 웃으면?",
            "options": ["감동", "감사", "감자칩", "웃감"],
            "answer": "감동"
        },
    ]
}

# 기분에 맞게 랜덤 퀴즈 선택
quiz = random.choice(quizzes[mood])

st.subheader("오늘의 유머 퀴즈 🤔")
st.write(quiz["question"])

# 보기 선택
choice = st.radio("정답을 골라보세요!", quiz["options"], key="quiz")

# 버튼 눌러서 확인
if st.button("정답 확인하기"):
    if choice == quiz["answer"]:
        st.success("🎉 정답이에요! 기분이 더 좋아지길 바라요!")
    else:
        st.error(f"😅 아쉽네요. 정답은 👉 {quiz['answer']} 입니다.")
