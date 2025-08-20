import streamlit as st

# session_state 초기화
# 'submitted' 상태가 session_state에 없으면 False로 초기화
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# MBTI 유형별 학습 스타일 설명
learning_styles = {
    "ISTJ": "현실적이고 체계적이어서, 명확한 목표와 계획에 따라 학습할 때 효율이 높습니다. 실제 사례와 데이터를 선호합니다.",
    "ISFJ": "따뜻하고 책임감이 강하며, 다른 사람을 돕는 과정에서 학습 동기를 얻습니다. 조용하고 안정적인 환경을 선호합니다.",
    "INFJ": "통찰력이 뛰어나고 이상주의적이며, 학습 내용이 갖는 의미와 가치를 중요하게 생각합니다. 창의적인 아이디어를 탐구하는 것을 좋아합니다.",
    "INTJ": "전략적이고 논리적이며, 복잡한 이론과 개념을 이해하는 데 뛰어납니다. 독립적으로 깊이 파고드는 학습을 선호합니다.",
    "ISTP": "논리적이고 실용적이어서, 직접 손으로 만지고 경험하며 배우는 것을 가장 좋아합니다. 문제 해결 과정 자체를 즐깁니다.",
    "ISFP": "온화하고 호기심이 많으며, 미적 감각이 뛰어납니다. 조화로운 분위기에서 자유롭게 자신의 관심사를 탐구하는 것을 선호합니다.",
    "INFP": "이상주의적이고 창의적이며, 자신의 가치관과 일치하는 내용을 배울 때 가장 몰입합니다. 상상력이 풍부합니다.",
    "INTP": "지적 호기심이 많고 논리적이어서, 복잡한 아이디어나 시스템의 원리를 파악하는 것을 즐깁니다. 추상적인 개념을 좋아합니다.",
    "ESTP": "에너지가 넘치고 실용적이어서, 직접 부딪히고 경험하며 배우는 것을 선호합니다. 활동적인 학습 환경에서 두각을 나타냅니다.",
    "ESFP": "사교적이고 활동적이어서, 다른 사람들과 함께 어울리며 즐겁게 배우는 것을 좋아합니다. 실제 경험을 중시합니다.",
    "ENFP": "열정적이고 상상력이 풍부하며, 다양한 가능성을 탐색하는 것을 즐깁니다. 긍정적인 분위기에서 창의력을 발휘합니다.",
    "ENTP": "독창적이고 논리적이어서, 지적인 도전을 즐기고 새로운 아이디어를 탐구하는 것을 좋아합니다. 토론과 논쟁을 통해 학습합니다.",
    "ESTJ": "체계적이고 현실적이어서, 정해진 절차와 규칙에 따라 효율적으로 학습하는 것을 선호합니다. 실용적인 지식을 중요하게 생각합니다.",
    "ESFJ": "사교적이고 책임감이 강하며, 다른 사람들과 협력하고 조화로운 관계 속에서 학습할 때 능률이 오릅니다.",
    "ENFJ": "열정적이고 카리스마가 있으며, 다른 사람의 성장을 돕는 데서 보람을 느낍니다. 상호작용이 활발한 학습을 선호합니다.",
    "ENTJ": "전략적이고 리더십이 뛰어나며, 장기적인 목표를 세우고 체계적으로 지식을 습득합니다. 효율성을 중시합니다."
}

# 질문과 선택지 정의
questions = {
    "EI": {
        "question": "1. 처음 만나는 사람들과의 파티에 갔을 때, 당신은...",
        "options": {"주로 새로운 사람들과 대화하며 에너지를 얻는다.": "E", "소수의 익숙한 사람들과 깊은 대화를 나누며 에너지를 얻는다.": "I"},
    },
    "SN": {
        "question": "2. 새로운 기술을 배울 때, 당신은...",
        "options": {"실제 예제와 구체적인 사용법을 먼저 확인한다.": "S", "기본 원리와 전체적인 개념을 먼저 이해하려고 한다.": "N"},
    },
    "TF": {
        "question": "3. 친구가 코딩 문제를 도와달라고 할 때, 당신은...",
        "options": {"문제의 원인을 논리적으로 분석하고 해결책을 제시한다.": "T", "친구가 얼마나 답답하고 힘든지 공감하고 위로해 준다.": "F"},
    },
    "JP": {
        "question": "4. 코딩 프로젝트를 시작할 때, 당신은...",
        "options": {"전체 계획을 세우고 체계적으로 진행하는 것을 선호한다.": "J", "일단 시작하고 상황에 따라 유연하게 계획을 변경한다.": "P"},
    },
    "EI2": {
        "question": "5. 주말에 휴식을 취할 때, 당신은...",
        "options": {"친구들과 만나거나 야외 활동을 하며 재충전한다.": "E", "집에서 조용히 책을 읽거나 취미 생활을 하며 재충전한다.": "I"},
    },
    "SN2": {
        "question": "6. 설명서를 읽을 때, 당신은...",
        "options": {"단계별 지침을 꼼꼼히 따라 하는 편이다.": "S", "전체적인 그림을 파악한 후 세부 사항은 건너뛰는 편이다.": "N"},
    }
}

def calculate_mbti(answers):
    """
    사용자의 답변을 바탕으로 MBTI 유형을 계산하는 함수
    """
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
    for key, value in answers.items():
        if value:  # 답변이 있는 경우에만 점수 계산
            scores[value] += 1

    mbti = ""
    mbti += "E" if scores['E'] >= scores['I'] else "I"
    mbti += "S" if scores['S'] >= scores['N'] else "N"
    mbti += "T" if scores['T'] >= scores['F'] else "F"
    mbti += "J" if scores['J'] >= scores['P'] else "P"
    
    return mbti

def submitted_callback():
    """
    제출 버튼이 클릭되었을 때 호출되는 콜백 함수
    """
    st.session_state.submitted = True

# --- 앱 UI 구성 ---
st.title("MBTI 학습 유형 진단 🔎")
st.write("간단한 질문을 통해 자신의 학습 스타일과 맞는 MBTI 유형을 알아보세요!")

# 사용자의 답변을 저장할 딕셔너리
user_answers = {}

# st.form을 사용하여 모든 질문을 한 번에 제출받음
with st.form("mbti_form"):
    # 각 질문에 대해 라디오 버튼 생성
    for key, q in questions.items():
        # st.radio의 key는 고유해야 하므로 질문의 key(예: "EI")를 사용
        answer_text = st.radio(q["question"], options=q["options"].keys(), key=key)
        user_answers[key] = q["options"][answer_text]

    # 제출 버튼
    submit_button = st.form_submit_button("결과 확인하기", on_click=submitted_callback)

# 제출 버튼이 클릭되었고, session_state.submitted가 True이면 결과 표시
if st.session_state.submitted:
    mbti_result = calculate_mbti(user_answers)
    
    st.header(f"📈 당신의 MBTI 학습 유형은: {mbti_result}")
    
    # 결과에 해당하는 학습 스타일 설명을 찾아 출력
    if mbti_result in learning_styles:
        st.info(learning_styles[mbti_result])
    else:
        st.warning("결과에 해당하는 학습 스타일 정보를 찾을 수 없습니다.")

    st.write("---")
    st.write("*주의: 이 진단은 재미를 위한 간단한 테스트이며, 정식 MBTI 검사와는 다릅니다.*")