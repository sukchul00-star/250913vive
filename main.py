# main.py
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

# --- 옵션 및 데이터 ---
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
        {"question": "화가 풀리면 생기는 강은?", "options": ["한강", "냉강", "화강", "평강"], "answer": "평강"},
        {"question": "화난 연필이 하는 말은?", "options": ["지우지마!", "꺾지마!", "난 연필심이야!", "써!"], "answer": "지우지마!"},
        {"question": "못생긴 감자가 웃으면?", "options": ["감동", "감사", "감자칩", "웃감"], "answer": "감동"},
    ],
}

# --- 기분 제출 폼 ---
with st.form("mood_form"):
    mood = st.radio("오늘 기분은 어떤가요?", mood_options, index=0)
    submit = st.form_submit_button("제출하기")
    if submit:
        st.session_state.mood_submitted = True
        st.session_state.selected_mood = mood
        st.session_state.current_quiz = random.choice(quizzes[mood])
        st.session_state.answer_checked = False
        if "answer_choice" in st.session_state:
            del st.session_state["answer_choice"]

# --- 제출된 경우에만 메시지와 퀴즈 보이기 ---
if st.session_state.mood_submitted:
    selected_mood = st.session_state.selected_mood
    st.subheader("오늘의 메시지 💌")
    st.write(mood_messages[selected_mood])

    quiz = st.session_state.current_quiz
    if quiz is None:
        st.error("퀴즈를 불러오는 데 문제가 발생했습니다. 다시 제출해 주세요.")
    else:
        st.subheader("오늘의 유머 퀴즈 🤔")
        st.write(quiz["question"])

        choice = st.radio("정답을 골라보세요!", quiz["options"], key="answer_choice")

        if st.button("정답 확인하기", key="check_answer"):
            st.session_state.answer_checked = True
            if choice == quiz["answer"]:
                st.success("🎉 정답이에요! 기분이 더 좋아지길 바랄게요!")
            else:
                st.error(f"😅 아쉽네요. 정답은 👉 {quiz['answer']} 입니다.")

        if st.button("처음으로 돌아가기", key="reset"):
            st.session_state.mood_submitted = False
            st.session_state.selected_mood = None
            st.session_state.current_quiz = None
            st.session_state.answer_checked = False
            if "answer_choice" in st.session_state:
                del st.session_state["answer_choice"]
            st.experimental_rerun()
