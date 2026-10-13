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
    st.markdown("<p class='big-font'>직접 그리며 원의 비밀 찾기!</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-font'>아래 3개의 탭을 하나씩 누르며 미션을 해결해 보세요!</p>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["1️⃣ 반지름 찾기", "2️⃣ 나만의 원 만들기", "3️⃣ 컴퍼스 꽃 그리기"])
    
    # [미션 1] 기존 반지름 길이 확인 캔버스
    with tab1:
        html_code_1 = """
        <div style="text-align: center; font-family: 'Malgun Gothic', sans-serif; background-color: #F8FAFC; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <h3 id="inst1" style="color:#1E293B; word-break: keep-all;">미션: 파란색 테두리를 클릭해서 반지름을 그려보세요!</h3>
            <canvas id="canvas1" width="400" height="400" style="border:4px dashed #94A3B8; border-radius: 50%; cursor: pointer; background-color: white; margin: 15px 0; touch-action: none;"></canvas>
            <div id="msg1" style="min-height: 80px; font-weight:bold; color: #4F46E5; font-size: 20px; margin-top: 10px; word-break: keep-all; line-height: 1.4;"></div>
            <button onclick="resetCanvas1()" style="margin-top:15px; padding: 12px 30px; font-size: 18px; font-weight:bold; background-color:#F1F5F9; border:2px solid #CBD5E1; border-radius:10px; cursor: pointer; color:#475569; transition: all 0.2s;">다시 지우고 처음부터 하기</button>
        </div>
        <script>
            const canvas1 = document.getElementById('canvas1');
            const ctx1 = canvas1.getContext('2d');
            const inst1 = document.getElementById('inst1');
            const msg1 = document.getElementById('msg1');
            const cx1 = 200, cy1 = 200, r1 = 180;
            let radii1 = [];

            function getRandColor() { return `hsl(${Math.floor(Math.random() * 360)}, 70%, 45%)`; }

            function draw1() {
                ctx1.clearRect(0,0,400,400);
                ctx1.beginPath(); ctx1.arc(cx1, cy1, r1, 0, 2*Math.PI);
                ctx1.strokeStyle = '#3730A3'; ctx1.lineWidth = 4; ctx1.stroke();
                
                radii1.forEach(pt => {
                    ctx1.beginPath(); ctx1.moveTo(cx1, cy1); ctx1.lineTo(pt.x, pt.y);
                    ctx1.strokeStyle = pt.c; ctx1.lineWidth = 4; ctx1.stroke();
                    ctx1.beginPath(); ctx1.arc(pt.x, pt.y, 6, 0, 2*Math.PI);
                    ctx1.fillStyle = pt.c; ctx1.fill();
                    
                    ctx1.save(); ctx1.translate(cx1+(pt.x-cx1)/2, cy1+(pt.y-cy1)/2);
                    const txt = '5cm', tw = ctx1.measureText(txt).width;
                    ctx1.fillStyle = 'rgba(255,255,255,0.9)'; ctx1.fillRect(-tw/2-4, -12, tw+8, 24);
                    ctx1.fillStyle = '#1F2937'; ctx1.font = '18px "Malgun Gothic"';
                    ctx1.textAlign='center'; ctx1.textBaseline='middle'; ctx1.fillText(txt, 0, 0);
                    ctx1.restore();
                });
                ctx1.beginPath(); ctx1.arc(cx1, cy1, 8, 0, 2*Math.PI); ctx1.fillStyle = '#EF4444'; ctx1.fill();
            }

            function act1(x, y) {
                const dist = Math.sqrt((x-cx1)**2 + (y-cy1)**2);
                if(Math.abs(dist-r1) < 40) {
                    const a = Math.atan2(y-cy1, x-cx1);
                    radii1.push({x: cx1+r1*Math.cos(a), y: cy1+r1*Math.sin(a), c: getRandColor()});
                    msg1.innerHTML = `반지름을 ${radii1.length}개 그렸습니다.<br>어느 쪽으로 그어도 길이는 모두 <b>5cm</b>로 똑같아요!`;
                    draw1();
                } else {
                    msg1.innerHTML = "<span style='color:#EF4444;'>원의 파란색 테두리 위를 정확히 클릭(터치)해 보세요!</span>";
                }
            }

            function getPos1(e) {
                const r = canvas1.getBoundingClientRect();
                let cx = e.clientX, cy = e.clientY;
                if(e.touches && e.touches.length>0) { cx = e.touches[0].clientX; cy = e.touches[0].clientY; }
                return { x: (cx-r.left)*(canvas1.width/r.width), y: (cy-r.top)*(canvas1.height/r.height) };
            }

            canvas1.addEventListener('mousedown', e => { const p = getPos1(e); act1(p.x, p.y); });
            canvas1.addEventListener('touchstart', e => { e.preventDefault(); const p = getPos1(e); act1(p.x, p.y); }, {passive:false});
            
            function resetCanvas1() { radii1=[]; msg1.innerHTML=""; draw1(); }
            draw1();
        </script>
        """
        components.html(html_code_1, height=800)

    # [미션 2] 드래그하여 나만의 원 만들기
    with tab2:
        html_code_2 = """
        <div style="text-align: center; font-family: 'Malgun Gothic', sans-serif; background-color: #FEF3C7; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <h3 style="color:#92400E; word-break: keep-all; margin-top:0;">미션: 화면을 꾹 누른 채로 드래그해서 나만의 원을 만들어보세요!</h3>
            <canvas id="canvas2" width="500" height="400" style="border:4px solid #FCD34D; border-radius: 10px; cursor: crosshair; background-color: white; margin: 15px 0; width:100%; max-width:500px; touch-action: none;"></canvas>
            <div id="msg2" style="min-height: 50px; font-weight:bold; color: #B45309; font-size: 20px; margin-top: 10px; word-break: keep-all; line-height: 1.4;">반지름이 길어질수록 원이 어떻게 변할까요?</div>
            <button onclick="resetCanvas2()" style="margin-top:15px; padding: 12px 30px; font-size: 18px; font-weight:bold; background-color:#FFFBEB; border:2px solid #FCD34D; border-radius:10px; cursor: pointer; color:#92400E; transition: all 0.2s;">화면 지우기</button>
        </div>
        <script>
            const canvas2 = document.getElementById('canvas2');
            const ctx2 = canvas2.getContext('2d');
            const msg2 = document.getElementById('msg2');
            let isDrawing = false;
            let cx2 = 0, cy2 = 0;
            let myCircles = []; // {x, y, r, c}

            function getRandColor2() { return `hsl(${Math.floor(Math.random() * 360)}, 70%, 45%)`; }

            function getPos2(e) {
                const r = canvas2.getBoundingClientRect();
                let cx = e.clientX, cy = e.clientY;
                if(e.touches && e.touches.length>0) { cx = e.touches[0].clientX; cy = e.touches[0].clientY; }
                return { x: (cx-r.left)*(canvas2.width/r.width), y: (cy-r.top)*(canvas2.height/r.height) };
            }

            function redraw2(tempX = null, tempY = null) {
                ctx2.clearRect(0,0,canvas2.width,canvas2.height);
                
                // 기존 그려진 원들
                myCircles.forEach(c => {
                    ctx2.beginPath(); ctx2.arc(c.x, c.y, c.r, 0, 2*Math.PI);
                    ctx2.strokeStyle = c.c; ctx2.lineWidth = 3; ctx2.stroke();
                    ctx2.fillStyle = c.c + '33'; ctx2.fill(); // 투명도 추가
                    // 중심점
                    ctx2.beginPath(); ctx2.arc(c.x, c.y, 4, 0, 2*Math.PI); ctx2.fillStyle=c.c; ctx2.fill();
                });

                // 현재 그리고 있는 원
                if(isDrawing && tempX !== null && tempY !== null) {
                    const r = Math.sqrt((tempX-cx2)**2 + (tempY-cy2)**2);
                    ctx2.beginPath(); ctx2.arc(cx2, cy2, r, 0, 2*Math.PI);
                    ctx2.strokeStyle = '#EF4444'; ctx2.lineWidth = 4; ctx2.stroke();
                    
                    // 중심에서 현재 점까지 선 (반지름)
                    ctx2.beginPath(); ctx2.moveTo(cx2, cy2); ctx2.lineTo(tempX, tempY);
                    ctx2.setLineDash([5, 5]); ctx2.stroke(); ctx2.setLineDash([]);
                    
                    // 중심점
                    ctx2.beginPath(); ctx2.arc(cx2, cy2, 6, 0, 2*Math.PI); ctx2.fillStyle='#EF4444'; ctx2.fill();
                    
                    // 길이 계산 (대략 30px을 1cm로 가정)
                    let cm = (r / 30).toFixed(1);
                    msg2.innerHTML = `현재 <b>반지름 길이는 ${cm}cm</b> 입니다! 손을 떼면 완성됩니다.`;
                }
            }

            canvas2.addEventListener('mousedown', e => {
                const p = getPos2(e); cx2 = p.x; cy2 = p.y; isDrawing = true;
            });
            canvas2.addEventListener('mousemove', e => {
                if(!isDrawing) return;
                const p = getPos2(e); redraw2(p.x, p.y);
            });
            canvas2.addEventListener('mouseup', e => {
                if(!isDrawing) return;
                const p = getPos2(e);
                const r = Math.sqrt((p.x-cx2)**2 + (p.y-cy2)**2);
                if(r > 10) myCircles.push({x: cx2, y: cy2, r: r, c: getRandColor2()});
                isDrawing = false;
                msg2.innerHTML = "와! 예쁜 원이 만들어졌어요. <b>반지름이 길어질수록 원도 커진다는 사실!</b>";
                redraw2();
            });

            // 터치 지원
            canvas2.addEventListener('touchstart', e => {
                e.preventDefault(); const p = getPos2(e); cx2 = p.x; cy2 = p.y; isDrawing = true;
            }, {passive:false});
            canvas2.addEventListener('touchmove', e => {
                if(!isDrawing) return;
                e.preventDefault(); const p = getPos2(e); redraw2(p.x, p.y);
            }, {passive:false});
            canvas2.addEventListener('touchend', e => {
                if(!isDrawing) return;
                // touchend는 좌표를 가져오기 어려우므로 마지막 상태 저장
                isDrawing = false;
                msg2.innerHTML = "원을 완성했어요! 빈 곳을 눌러 다른 크기의 원도 그려보세요.";
            });

            function resetCanvas2() { myCircles=[]; msg2.innerHTML="화면을 꾹 누른 채로 드래그해서 나만의 원을 만들어보세요!"; redraw2(); }
            redraw2();
        </script>
        """
        components.html(html_code_2, height=800)

    # [미션 3] 컴퍼스 꽃 무늬 그리기
    with tab3:
        html_code_3 = """
        <div style="text-align: center; font-family: 'Malgun Gothic', sans-serif; background-color: #ECFCCB; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <h3 style="color:#3F6212; word-break: keep-all; margin-top:0;">미션: 테두리를 클릭하며 예쁜 컴퍼스 꽃을 피워보세요!</h3>
            <canvas id="canvas3" width="500" height="400" style="border:4px solid #84CC16; border-radius: 10px; cursor: pointer; background-color: white; margin: 15px 0; width:100%; max-width:500px; touch-action: none;"></canvas>
            <div id="msg3" style="min-height: 50px; font-weight:bold; color: #4D7C0F; font-size: 20px; margin-top: 10px; word-break: keep-all; line-height: 1.4;">중앙에 있는 검은색 원의 테두리(원주) 아무 곳이나 클릭해 보세요.</div>
            <button onclick="resetCanvas3()" style="margin-top:15px; padding: 12px 30px; font-size: 18px; font-weight:bold; background-color:#F7FEE7; border:2px solid #84CC16; border-radius:10px; cursor: pointer; color:#3F6212; transition: all 0.2s;">다시 지우고 처음부터 하기</button>
        </div>
        <script>
            const canvas3 = document.getElementById('canvas3');
            const ctx3 = canvas3.getContext('2d');
            const msg3 = document.getElementById('msg3');
            const rootX = 250, rootY = 200, r3 = 70;
            let flowerCircles = []; // 중심점들 저장

            function getRandColor3() { return `hsl(${Math.floor(Math.random() * 360)}, 70%, 45%)`; }

            function draw3() {
                ctx3.clearRect(0,0,canvas3.width,canvas3.height);
                
                // 중심 원 그리기
                ctx3.beginPath(); ctx3.arc(rootX, rootY, r3, 0, 2*Math.PI);
                ctx3.strokeStyle = '#1F2937'; ctx3.lineWidth = 3; ctx3.stroke();
                ctx3.beginPath(); ctx3.arc(rootX, rootY, 5, 0, 2*Math.PI); ctx3.fillStyle='#1F2937'; ctx3.fill();

                // 추가된 원들 그리기
                flowerCircles.forEach(c => {
                    ctx3.beginPath(); ctx3.arc(c.x, c.y, r3, 0, 2*Math.PI);
                    ctx3.strokeStyle = c.c; ctx3.lineWidth = 2; ctx3.stroke();
                    // 중심점 표시
                    ctx3.beginPath(); ctx3.arc(c.x, c.y, 4, 0, 2*Math.PI); ctx3.fillStyle=c.c; ctx3.fill();
                });
            }

            function getPos3(e) {
                const r = canvas3.getBoundingClientRect();
                let cx = e.clientX, cy = e.clientY;
                if(e.touches && e.touches.length>0) { cx = e.touches[0].clientX; cy = e.touches[0].clientY; }
                return { x: (cx-r.left)*(canvas3.width/r.width), y: (cy-r.top)*(canvas3.height/r.height) };
            }

            function act3(x, y) {
                // 클릭한 곳이 중앙 원의 테두리 부근인지 확인
                const dist = Math.sqrt((x-rootX)**2 + (y-rootY)**2);
                if(Math.abs(dist - r3) < 25) { // 오차 범위 허용
                    // 클릭한 점의 정확한 원주 위 좌표 계산 (예쁘게 그려지도록 보정)
                    const angle = Math.atan2(y-rootY, x-rootX);
                    const exactX = rootX + r3 * Math.cos(angle);
                    const exactY = rootY + r3 * Math.sin(angle);
                    
                    flowerCircles.push({x: exactX, y: exactY, c: getRandColor3()});
                    draw3();
                    
                    if(flowerCircles.length >= 6) {
                        msg3.innerHTML = "우와! <b>반지름이 같은 원들</b>이 모여 아름다운 꽃 무늬가 완성되었어요!";
                    } else {
                        msg3.innerHTML = `테두리를 중심으로 반지름이 똑같은 새 원이 생겼어요! (${flowerCircles.length}개 잎사귀)`;
                    }
                } else {
                    msg3.innerHTML = "<span style='color:#EF4444;'>가운데 있는 <b>검은색 원의 테두리</b>를 클릭해야 해요!</span>";
                }
            }

            canvas3.addEventListener('mousedown', e => { const p = getPos3(e); act3(p.x, p.y); });
            canvas3.addEventListener('touchstart', e => { e.preventDefault(); const p = getPos3(e); act3(p.x, p.y); }, {passive:false});
            
            function resetCanvas3() { flowerCircles=[]; msg3.innerHTML="중앙에 있는 검은색 원의 테두리(원주) 아무 곳이나 클릭해 보세요."; draw3(); }
            draw3();
        </script>
        """
        components.html(html_code_3, height=800)
    
    st.write("")
    st.markdown("---")
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("원리를 모두 깨달았으니 퀴즈 풀기 ➡️", use_container_width=True):
            go_to('quiz')
            st.rerun()

# === 퀴즈 화면 ===
elif st.session_state.current_view == 'quiz':
    progress = (st.session_state.question_index) / len(questions)
    st.progress(progress)
    
    current_q = questions[st.session_state.question_index]
    
    st.markdown(f"""
    <div style='background-color:white; padding:30px; border-radius:15px; border:3px solid #E0E7FF; margin-bottom:30px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
        <h3 style='color:#1F2937; text-align:center; margin:0; line-height:1.5; word-break:keep-all;'>Q{st.session_state.question_index + 1}.<br>{current_q['question']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(len(current_q['options']))
    for i, option in enumerate(current_q['options']):
        with cols[i]:
            if st.button(option, key=f"opt_{st.session_state.question_index}_{i}", use_container_width=True, disabled=st.session_state.feedback is not None):
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
            if st.button(btn_text, key="next_btn", use_container_width=True):
                next_question()
                st.rerun()

# === 결과 화면 ===
elif st.session_state.current_view == 'result':
    st.balloons()
    st.markdown("<p class='big-font'>원 단원 정복 완료!</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style='background-color:#FEF3C7; padding:40px; border-radius:20px; text-align:center; border:5px solid #FCD34D; margin:30px 0; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);'>
        <p style='font-size:26px; color:#92400E; margin-bottom:15px; font-weight:bold;'>내 점수는?</p>
        <p style='font-size:80px; font-weight:900; color:#B45309; margin:0;'>{st.session_state.score} <span style='font-size:35px;'>점</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='sub-font'>이제 컴퍼스로 원을 아주 잘 그릴 수 있겠어요!</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🔄 처음부터 다시하기", use_container_width=True):
            reset_quiz()
            st.rerun()
