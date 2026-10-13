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
        margin-bottom: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .main-header h2 {
        color: white !important;
        text-align: center;
        margin: 0;
        font-size: 28px !important;
        word-break: keep-all;
    }

    /* 공통 버튼 스타일 */
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
        margin-bottom: 10px;
    }
    .sub-font {
        text-align:center; 
        font-size:20px; 
        color:#4B5563;
        margin-bottom: 30px;
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
    
    /* 탭 스타일 개선 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: pre-wrap;
        background-color: #F8FAFC;
        border-radius: 10px 10px 0 0;
        border: 2px solid transparent;
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #EEF2FF;
        border: 2px solid #4F46E5;
        border-bottom: none;
        color: #4F46E5;
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
    st.session
