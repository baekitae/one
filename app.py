import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="녹산초 3학년 수학 탐험대",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS 적용 (UI 및 버튼 간격 완벽 개선)
st.markdown("""
    <style>
    /* 전체 여백 조정 */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 800px;
    }
    
    /* 헤더 스타일 */
    .main-header {
        background: linear-gradient(135deg, #4F46E5, #6366F1);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 40px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .main-header h2 {
        color: white !important;
        text-align: center;
        margin: 0;
        font-size: 28px !important;
        word-break: keep-all;
    }

    /* 공통 버튼 스타일 (가운데 정렬 및 크기 최적화) */
    .stButton>button {
        width: 100% !important;
        min-height: 100px;
        font-size: 22px !important;
        font-weight: bold;
        border-radius: 15px;
        border: 2px solid #4F46E5;
        background-color: white;
        color: #4F46E5;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        word-break: keep-all;
        padding: 10px;
    }
    .stButton>button p {
        margin: 0 !important;
        text-align: center !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stButton>button:hover {
        background-color: #4F46E5;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    .stButton>button:active {
        transform: translateY(0);
    }
    
    /* 텍스트 스타일 */
    .big-font {
        font-size:32px !important;
        font-weight: 800;
        color: #3730A3;
        text-align: center;
        margin-bottom: 15px;
    }
    .sub-font {
        text-align:center; 
        font-size:20px; 
        color:#4B5563;
        margin-bottom: 40px;
        word-break: keep-all;
    }

    /* 개념 박스 스타일 */
    .concept-box {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-left: 6px solid #4F46E5;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 세션 상태 초기화
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'home'
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'feedback' not in st.session_state:
    st.session_state.feedback = None

# 퀴즈 데이터
questions = [
    {
        "question": "원을 그릴 때 컴퍼스의 뾰족한 침을 꽂는, 원의 한가운데 있는 점을 무엇이라고 부를까요?",
        "options": ["원의 중심", "반지름", "지름"],
        "answer": "원의 중심"
    },
    {
        "question": "원의 중심과 원 위의 한 점을 이은 선분을 무엇이라고 할까요?",
        "options": ["원의 중심", "반지름", "지름"],
        "answer": "반지름"
    },
    {
        "question": "반지름이 5cm인 원이 있습니다. 이 원의 지름은 몇 cm일까요?",
        "options": ["5cm", "10cm", "15cm"],
        "answer": "10cm"
    },
    {
        "question": "지름이 14cm인 원의 반지름은 몇 cm일까요?",
        "options": ["7cm", "14cm", "28cm"],
        "answer": "7cm"
    },
    {
        "question": "한 원 안에서 그려진 여러 반지름의 길이는 어떨까요?",
        "options": ["모두 같습니다", "모두 다릅니다", "알 수 없습니다"],
        "answer": "모두 같습니다"
    }
]

# 화면 이동 함수
def go_to(view):
    st.session_state.current_view = view
    st.session_state.feedback = None

def reset_quiz():
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.feedback = None
    st.session_state.current_view = 'home'

def check_answer(selected_option):
    if st.session_state.feedback is None: 
        correct_answer = questions[st.session_state.question_index]['answer']
        if selected_option == correct_answer:
            st.session_state.feedback = 'correct'
            st.session_state.score += 20
        else:
            st.session_state.feedback = 'incorrect'

def next_question():
    st.session_state.feedback = None
    if st.session_state.question_index < len(questions) - 1:
        st.session_state.question_index += 1
    else:
        st.session_state.current_view = 'result'

# === 헤더 영역 ===
st.markdown("<div class='main-header'><h2>🎯 녹산초 3학년 수학 탐험대:<br>원의 비밀을 찾아라!</h2></div>", unsafe_allow_html=True)

# === 홈 화면 ===
if st.session_state.current_view == 'home':
    st.markdown("<p class='big-font'>동그란 원의 비밀!</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-font'>3학년 2학기 2단원, 원의 중심과 반지름, 지름에 대해 알아볼까요?</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 개념 먼저 배우기", use_container_width=True):
            go_to('concept')
            st.rerun()
    with col2:
        if st.button("✏️ 바로 퀴즈 풀기", use_container_width=True):
            go_to('quiz')
            st.rerun()

# === 개념 학습 화면 ===
elif st.session_state.current_view == 'concept':
    st.markdown("<p class='big-font'>원의 핵심 개념 3가지</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='concept-box'>
        <h4 style='color:#EF4444; margin-top:0;'>📍 원의 중심</h4>
        <p style='font-size:18px; margin-bottom:0;'>원을 그릴 때 컴퍼스의 침을 꽂는 원의 <b>한가운데 점</b>이에요.</p>
    </div>
    <div class='concept-box' style='border-left-color:#10B981;'>
        <h4 style='color:#10B981; margin-top:0;'>📏 반지름</h4>
        <p style='font-size:18px; margin-bottom:0;'>원의 중심과 원 위의 한 점을 이은 선분이에요. <b>길이는 모두 같아요!</b></p>
    </div>
    <div class='concept-box' style='border-left-color:#F59E0B;'>
        <h4 style='color:#F59E0B; margin-top:0;'>↔️ 지름</h4>
        <p style='font-size:18px; margin-bottom:0;'>원의 중심을 지나며 원 위의 두 점을 이은 선분이에요. <b>반지름의 딱 2배</b>예요!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("직접 그려보며 확인하기 ➡️", use_container_width=True):
            go_to('activity')
            st.rerun()

# === 직접 체험하기(Activity) 화면 ===
elif st.session_state.current_view == 'activity':
    st.markdown("<p class='big-font'>내가 직접 그리는 반지름!</p>", unsafe_allow_html=True)
    
    # 단위가 'cm'로 고정되고, 캔버스 전체 높이를 800px로 넉넉하게 늘린 코드
    html_code = """
    <div style="text-align: center; font-family: 'Malgun Gothic', sans-serif; background-color: #F8FAFC; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h3 id="instruction" style="color:#1E293B; word-break: keep-all;">미션 1: 원의 가장 한가운데(중심)를 찾아 클릭하세요!</h3>
        <canvas id="mathCanvas" width="400" height="400" style="border:4px dashed #94A3B8; border-radius: 50%; cursor: pointer; background-color: white; margin: 15px 0; touch-action: none;"></canvas>
        <div id="message" style="min-height: 80px; font-weight:bold; color: #4F46E5; font-size: 20px; margin-top: 10px; word-break: keep-all; line-height:
