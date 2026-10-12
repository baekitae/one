import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="녹산초 3학년 수학 탐험대",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 커스텀 CSS 적용
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 15px;
        border: 2px solid #4F46E5;
        background-color: white;
        color: #4F46E5;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #4F46E5;
        color: white;
        border: 2px solid #4F46E5;
    }
    .stButton>button:active {
        background-color: #4338CA;
        color: white;
    }
    div[data-testid="stHorizontalBlock"] button {
        background-color: #EEF2FF;
    }
    div[data-testid="stHorizontalBlock"] button:hover {
        background-color: #C7D2FE;
        color: #3730A3;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #3730A3;
        text-align: center;
        margin-bottom: 20px;
    }
    .concept-box {
        background-color: #EEF2FF;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-left: 5px solid #4F46E5;
    }
    .score-box {
        background-color: #FEF3C7;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 4px solid #FCD34D;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 세션 상태 초기화
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'home' # home, concept, activity, quiz, result
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
        "question": "반지름이 4cm인 원이 있습니다. 이 원의 지름은 몇 cm일까요?",
        "options": ["4cm", "8cm", "12cm"],
        "answer": "8cm"
    },
    {
        "question": "지름이 10cm인 원의 반지름은 몇 cm일까요?",
        "options": ["5cm", "10cm", "20cm"],
        "answer": "5cm"
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
st.markdown("<div style='background-color:#4F46E5; padding:15px; border-radius:10px; margin-bottom:30px;'><h2 style='color:white; text-align:center; margin:0;'>🎯 녹산초 3학년 수학 탐험대: 원의 비밀을 찾아라!</h2></div>", unsafe_allow_html=True)

# === 홈 화면 ===
if st.session_state.current_view == 'home':
    st.markdown("<p class='big-font'>동그란 원의 비밀!</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:18px; color:#4B5563;'>3학년 2학기 2단원, 원의 중심과 반지름, 지름에 대해 알아볼까요?</p>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 개념 먼저 배우기"):
            go_to('concept')
            st.rerun()
    with col2:
        if st.button("✏️ 바로 퀴즈 풀기"):
            go_to('quiz')
            st.rerun()

# === 개념 학습 화면 ===
elif st.session_state.current_view == 'concept':
    st.markdown("<p class='big-font'>원의 핵심 개념 3가지</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='concept-box'>
        <h4 style='color:#EF4444;'>📍 원의 중심</h4>
        <p style='font-size:18px;'>원을 그릴 때 컴퍼스의 침을 꽂는 원의 <b>한가운데 점</b>이에요.</p>
    </div>
    <div class='concept-box' style='border-left-color:#10B981;'>
        <h4 style='color:#10B981;'>📏 반지름</h4>
        <p style='font-size:18px;'>원의 중심과 원 위의 한 점을 이은 선분이에요. <b>길이는 모두 같아요!</b></p>
    </div>
    <div class='concept-box' style='border-left-color:#F59E0B;'>
        <h4 style='color:#F59E0B;'>↔️ 지름</h4>
        <p style='font-size:18px;'>원의 중심을 지나며 원 위의 두 점을 이은 선분이에요. <b>반지름의 딱 2배</b>예요!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("직접 그려보며 확인하기 ➡️"):
        go_to('activity')
        st.rerun()

# === 직접 체험하기(Activity) 화면 ===
elif st.session_state.current_view == 'activity':
    st.markdown("<p class='big-font'>내가 직접 원의 중심과 반지름 찾기!</p>", unsafe_allow_html=True)
    
    # HTML5 Canvas와 JavaScript를 이용한 인터랙티브 그리기 영역
    html_code = """
    <div style="text-align: center; font-family: 'Malgun Gothic', sans-serif; background-color: #F8FAFC; padding: 20px; border-radius: 15px;">
        <h3 id="instruction" style="color:#1E293B;">미션 1: 원의 가장 한가운데(중심)를 찾아 클릭(터치)하세요!</h3>
        <canvas id="mathCanvas" width="400" height="400" style="border:4px dashed #94A3B8; border-radius: 50%; cursor: pointer; background-color: white; margin: 10px 0;"></canvas>
        <div id="message" style="min-height: 60px; font-weight:bold; color: #4F46E5; font-size: 20px; margin-top: 10px;"></div>
        <button onclick="resetCanvas()" style="margin-top:10px; padding: 10px 25px; font-size: 18px; font-weight:bold; background-color:#F1F5F9; border:2px solid #CBD5E1; border-radius:10px; cursor: pointer; color:#475569;">다시 지우고 처음부터 하기</button>
    </div>
    
    <script>
        const canvas = document.getElementById('mathCanvas');
        const ctx = canvas.getContext('2d');
        const instruction = document.getElementById('instruction');
        const message = document.getElementById('message');

        const centerX = 200;
        const centerY = 200;
        const radius = 180;

        let isCenterFound = false;
        let drawnRadii = [];

        function drawBase() {
            ctx.clearRect(0, 0, 400, 400);
            
            // 기본 원 그리기
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
            ctx.strokeStyle = '#3730A3';
            ctx.lineWidth = 4;
            ctx.stroke();

            // 중심이 찾아졌다면 빨간 점 그리기
            if (isCenterFound) {
                ctx.beginPath();
                ctx.arc(centerX, centerY, 8, 0, 2 * Math.PI);
                ctx.fillStyle = '#EF4444';
                ctx.fill();
            }

            // 그려진 반지름들 표시하기
            drawnRadii.forEach((pt, index) => {
                ctx.beginPath();
                ctx.moveTo(centerX, centerY);
                ctx.lineTo(pt.x, pt.y);
                ctx.strokeStyle = '#10B981';
                ctx.lineWidth = 4;
                ctx.stroke();

                ctx.beginPath();
                ctx.arc(pt.x, pt.y, 6, 0, 2*Math.PI);
                ctx.fillStyle = '#10B981';
                ctx.fill();
            });
        }

        canvas.addEventListener('mousedown', function(e) {
            const rect = canvas.getBoundingClientRect();
            // 크롬북 터치 및 마우스 스케일 보정
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            const x = (e.clientX - rect.left) * scaleX;
            const y = (e.clientY - rect.top) * scaleY;

            if (!isCenterFound) {
                const dist = Math.sqrt((x - centerX)**2 + (y - centerY)**2);
                if (dist < 30) {
                    isCenterFound = true;
                    instruction.innerHTML = "미션 2: 원의 테두리(둘레)를 클릭해서 선을 그어보세요!";
                    message.innerHTML = "정확해요! 빨간색 점이 바로 <b>'원의 중심'</b>입니다.";
                    drawBase();
                } else {
                    message.innerHTML = "<span style='color:#EF4444;'>조금 더 정중앙을 클릭해 보세요!</span>";
                }
            } else {
                const dist = Math.sqrt((x - centerX)**2 + (y - centerY)**2);
                if (Math.abs(dist - radius) < 40) {
                    const angle = Math.atan2(y - centerY, x - centerX);
                    const edgeX = centerX + radius * Math.cos(angle);
                    const edgeY = centerY + radius * Math.sin(angle);
                    drawnRadii.push({x: edgeX, y: edgeY});
                    
                    if (drawnRadii.length === 1) {
                        message.innerHTML = "이 초록색 선이 <b>'반지름'</b>입니다!<br>테두리를 여러 번 눌러 반지름을 더 그려보세요.";
                        instruction.innerHTML = "미션 3: 한 원에서 반지름의 길이는 모두 같을까요?";
                    } else {
                        message.innerHTML = `반지름을 ${drawnRadii.length}개 그렸습니다.<br><b>직접 보니 어때요? 한 원에서 반지름의 길이는 모두 같아요!</b>`;
                    }
                    drawBase();
                } else {
                    message.innerHTML = "<span style='color:#EF4444;'>원의 테두리(파란색 선) 위를 정확히 클릭해 보세요!</span>";
                }
            }
        });

        // 모바일 및 크롬북 터치 이벤트 지원
        canvas.addEventListener('touchstart', function(e) {
            e.preventDefault();
            const touch = e.touches[0];
            const mouseEvent = new MouseEvent('mousedown', {
                clientX: touch.clientX,
                clientY: touch.clientY
            });
            canvas.dispatchEvent(mouseEvent);
        });

        function resetCanvas() {
            isCenterFound = false;
            drawnRadii = [];
            instruction.innerHTML = "미션 1: 원의 가장 한가운데(중심)를 찾아 클릭(터치)하세요!";
            message.innerHTML = "";
            drawBase();
        }

        drawBase();
    </script>
    """
    components.html(html_code, height=600)
    
    st.write("")
    if st.button("원리도 깨달았으니 퀴즈 풀러 가기 ➡️"):
        go_to('quiz')
        st.rerun()

# === 퀴즈 화면 ===
elif st.session_state.current_view == 'quiz':
    progress = (st.session_state.question_index) / len(questions)
    st.progress(progress)
    
    current_q = questions[st.session_state.question_index]
    
    st.markdown(f"<div style='background-color:white; padding:20px; border-radius:15px; border:2px solid #E0E7FF; margin-bottom:30px;'><h3 style='color:#1F2937; text-align:center;'>Q{st.session_state.question_index + 1}. {current_q['question']}</h3></div>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, option in enumerate(current_q['options']):
        with cols[i]:
            if st.button(option, key=f"opt_{st.session_state.question_index}_{i}", disabled=st.session_state.feedback is not None):
                check_answer(option)
                st.rerun()
                
    if st.session_state.feedback:
        st.write("")
        if st.session_state.feedback == 'correct':
            st.success("🎉 참 잘했어요! 정답입니다.")
        else:
            st.error(f"😅 아쉽네요. 정답은 [ {current_q['answer']} ] 입니다.")
            
        st.write("")
        btn_text = "다음 문제 ➡️" if st.session_state.question_index < len(questions) - 1 else "결과 보기 🏆"
        
        _, col_btn, _ = st.columns([1, 2, 1])
        with col_btn:
            if st.button(btn_text, key="next_btn"):
                next_question()
                st.rerun()

# === 결과 화면 ===
elif st.session_state.current_view == 'result':
    st.balloons()
    st.markdown("<p class='big-font'>원 단원 정복 완료!</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='score-box'>
        <p style='font-size:24px; color:#4B5563; margin-bottom:10px;'>내 점수는?</p>
        <p style='font-size:70px; font-weight:900; color:#4F46E5; margin:0;'>{st.session_state.score} <span style='font-size:30px;'>점</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='text-align:center; font-size:20px; color:#4B5563; margin-bottom:30px;'>이제 컴퍼스로 원을 아주 잘 그릴 수 있겠어요!</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🔄 처음부터 다시하기"):
            reset_quiz()
            st.rerun()
