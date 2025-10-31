import streamlit as st
import textwrap

# --- 1. 개념 데이터베이스 및 LLM 응답 시뮬레이션 함수 ---

# 각 개념에 대한 상세 설명 (줄바꿈 \n을 이용하여 여러 줄의 논리적 문단으로 구성)
# 모든 개념의 최대 길이는 3줄로 통일합니다.
CONCEPT_EXPLANATIONS = {
    "유리함수": (
        "유리함수는 두 다항식 P(x)와 Q(x)에 대하여 $y = \\frac{P(x)}{Q(x)}$ 형태로 나타낼 수 있는 함수입니다.\\n"
        "단, 분모 다항식 $Q(x)$는 0이 아니어야 합니다.\\n"
        "다항함수($y=x^2$ 등)도 유리함수에 포함되지만, 보통 분모에 변수 $x$가 있는 분수함수를 의미합니다."
    ),
    "정의역": (
        "유리함수 $y = \\frac{P(x)}{Q(x)}$에서 함수가 정의되기 위한 $x$ 값들의 집합을 정의역이라고 합니다.\\n"
        "함수값이 존재하려면 분모 $Q(x)$가 0이 되면 안 됩니다.\\n"
        "따라서 정의역은 $\{\\, x \\mid Q(x) \\neq 0 \\, \}$ 이며, 이는 수직 점근선을 제외한 부분입니다."
    ),
    "치역": (
        "함수 $y = f(x)$에서 정의역의 원소 $x$에 대응되는 함숫값 $f(x)$들의 집합을 치역이라고 합니다.\\n"
        "유리함수의 경우, 그래프의 수평 점근선 $y=q$를 제외한 모든 실수 값을 치역으로 가집니다.\\n"
        "즉, 치역은 $\{\\, y \\mid y \\neq q \\, \}$ 형태입니다."
    ),
    "공역": (
        "공역은 함수 $f(x)$의 함숫값 $y$가 될 수 있는 모든 원소들의 집합입니다.\\n"
        "이는 함수를 정의할 때 미리 지정하는 $Y$ 집합을 의미하며, 치역은 이 공역의 부분집합입니다.\\n"
        "유리함수를 실수 전체에서 다룰 때, 별도의 언급이 없다면 공역은 보통 실수 전체의 집합 $\\mathbb{R}$입니다."
    ),
    "점근선": (
        "점근선은 유리함수의 그래프가 한없이 가까워지지만, 절대 닿지 않는 선입니다.\\n"
        "함수가 정의되지 않는 $x$ 값(수직 점근선)과 함숫값이 될 수 없는 $y$ 값(수평 점근선)에 의해 결정됩니다.\\n"
        "표준형 $y = \\frac{k}{x-p} + q$ 에서 수직 점근선은 $x=p$, 수평 점근선은 $y=q$ 입니다."
    ),
    "일반형": (
        "유리함수의 일반형은 $y = \\frac{ax+b}{cx+d}$ 입니다.\\n"
        "이 형태에서는 점근선이나 그래프의 특징을 바로 알기 어렵습니다.\\n"
        "따라서 그래프를 정확히 분석하고 그리기 위해서는 표준형으로 변환하는 과정이 필수입니다."
    ),
    "표준형": (
        "유리함수의 표준형은 $y = \\frac{k}{x-p} + q$ 형태이며, 함수를 분석하는 데 가장 유용한 형태입니다.\\n"
        "$x=p$는 수직 점근선, $y=q$는 수평 점근선이 됩니다.\\n"
        "$k$는 그래프의 모양과 방향을 결정하며, $k$의 절댓값이 클수록 원점에서 멀어집니다."
    )
}

# 퀴즈 데이터 (질문, 정답(True=O, False=X), 해설)
QUIZ_QUESTIONS = {
    "유리함수": {
        "question": "유리함수 $y = \\frac{x^2}{x-1}$의 그래프는 무조건 곡선 형태이다.",
        "answer": False,
        "explanation": "유리함수 중 분모가 상수인 경우(예: $y=x^2$)는 다항함수(포물선)가 되므로, 무조건 곡선 형태인 것은 아닙니다.",
        "correct_choice": "X"
    },
    "정의역": {
        "question": "함수 $f(x) = \\frac{3}{x+2}$의 정의역은 $x \\neq 2$인 모든 실수이다.",
        "answer": False,
        "explanation": "정의역은 분모가 0이 되지 않게 하는 $x$ 값들의 집합이므로, $x+2=0$, 즉 $x=-2$를 제외한 모든 실수입니다.",
        "correct_choice": "X"
    },
    "치역": {
        "question": "표준형 $y = \\frac{k}{x-p} + q$에서 치역은 $y \\neq q$인 모든 실수이다.",
        "answer": True,
        "explanation": "수평 점근선 $y=q$는 함숫값이 될 수 없는 값이므로, 치역은 $y$가 $q$가 아닌 모든 실수의 집합입니다.",
        "correct_choice": "O"
    },
    "공역": {
        "question": "함수 $f: X \\to Y$에서, 집합 $Y$를 '공역'이라고 부른다. 치역은 항상 공역과 같다.",
        "answer": False,
        "explanation": "치역은 공역의 부분집합이며, 치역이 공역 전체와 같을 수도 있지만 일반적으로는 다를 수 있습니다.",
        "correct_choice": "X"
    },
    "점근선": {
        "question": "유리함수 $y = \\frac{2x-1}{x+3}$의 수직 점근선은 $x=-3$이고, 수평 점근선은 $y=2$이다.",
        "answer": True,
        "explanation": "수직 점근선은 분모 $x+3=0$에서 $x=-3$이고, 수평 점근선은 $\\frac{x$항 계수}}{x$항 계수}} = \\frac{2}{1} = 2$이므로 $y=2$입니다.",
        "correct_choice": "O"
    },
    "일반형": {
        "question": "유리함수의 일반형 $y = \\frac{ax+b}{cx+d}$만으로도 점근선을 바로 파악할 수 있다.",
        "answer": False,
        "explanation": "일반형에서는 점근선을 파악하기 어렵기 때문에, 보통 분자/분모 나누기 과정을 통해 표준형으로 변환해야 합니다.",
        "correct_choice": "X"
    },
    "표준형": {
        "question": "표준형 $y = \\frac{-3}{x+1} - 5$의 그래프는 제 2, 4사분면의 형태를 가진다.",
        "answer": False,
        "explanation": "표준형에서 $k=-3$으로 음수이므로, 그래프는 점근선의 교점 $(-1, -5)$를 기준으로 제 2, 4사분면 형태(새로운 좌표축 기준)를 가집니다. 일반적인 1, 2, 3, 4 사분면과는 관련이 적습니다.",
        "correct_choice": "X"
    }
}

def get_concept_summary(concept_name: str, length: int) -> str:
    """
    사용자가 요청한 개념에 대한 설명을 가져오고, 지정된 줄 수로 요약(시뮬레이션)합니다.
    """
    if concept_name not in CONCEPT_EXPLANATIONS:
        # 개념이 없을 경우 에러 메시지 반환
        return f"죄송합니다. **{concept_name}**에 대한 개념 설명은 준비되어 있지 않습니다. '유리함수', '정의역', '치역', '공역', '점근선', '일반형', '표준형' 중 하나를 입력해 주세요."

    full_text = CONCEPT_EXPLANATIONS[concept_name]

    # 텍스트를 논리적인 줄(줄바꿈 \n 기준)로 분리합니다.
    lines = full_text.split('\\n')

    # 요청된 길이만큼의 줄만 선택합니다.
    summarized_lines = lines[:length]

    # 선택된 줄들을 다시 줄바꿈 문자(Markdown 줄바꿈을 위해 띄어쓰기 2개 후 \n)로 연결합니다.
    summary = "  \n".join(summarized_lines)

    return summary

# --- 2. Streamlit UI 구성 ---

st.set_page_config(
    page_title="유리함수 개념 튜터",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("📚 유리함수 개념 학습 및 퀴즈 도우미")
st.markdown("---")

# ==============================================================================
# 섹션 1: 개념 학습
# ==============================================================================
st.header("1. 🎓 개념 학습: 정의와 특징")
st.markdown(
    "유리함수의 7가지 핵심 개념을 입력하고, 아래 슬라이더로 원하는 설명 길이를 조절해 보세요."
)

# 사용자 입력 및 슬라이더
col1, col2 = st.columns([2, 1])

with col1:
    # 텍스트 입력창
    concept_input = st.text_input(
        "궁금한 개념을 입력하세요 (예: 점근선, 표준형, 공역)",
        value="공역", # 초기값을 '공역'으로 설정
        key="concept_input_key"
    ).strip() # 앞뒤 공백 제거

with col2:
    # 설명 길이 슬라이드바
    summary_length = st.slider(
        "설명 글의 길이 설정 (줄 수)",
        min_value=1,
        max_value=3, # 최대값 3으로 유지
        value=3, # 기본값 3으로 유지
        step=1,
        key="summary_length_key"
    )

st.subheader(f"🔍 개념 설명: {concept_input if concept_input else '개념을 입력해 주세요'}")

if concept_input:
    # 개념 설명 함수 호출
    explanation = get_concept_summary(concept_input, summary_length)

    # Markdown으로 결과 출력
    st.markdown(explanation)

    # 입력된 개념이 유효할 경우, 수식 렌더링을 위해 st.latex를 사용
    if concept_input in ["유리함수", "일반형", "표준형", "점근선"]:
        st.subheader("💡 관련 수학 공식")
        if concept_input == "유리함수":
            st.latex("y = \\frac{P(x)}{Q(x)}, \\quad (Q(x) \\neq 0)")
        elif concept_input == "일반형":
            st.latex("y = \\frac{ax+b}{cx+d} \\quad \\rightarrow \\quad (c \\neq 0, ad-bc \\neq 0)")
        elif concept_input == "표준형" or concept_input == "점근선":
            st.latex("y = \\frac{k}{x-p} + q \\quad \\rightarrow \\quad (점근선: x=p, y=q)")

st.markdown("---")
st.markdown("---")

# ==============================================================================
# 섹션 2: O/X 퀴즈
# ==============================================================================
st.header("2. ✅ 개념 이해 O/X 퀴즈")
st.info("개념을 선택하고 O/X 퀴즈를 풀어보세요. 정답을 확인하면 해설이 나타납니다.")

quiz_options = [
    "1. 유리함수",
    "2. 정의역",
    "3. 치역",
    "4. 공역",
    "5. 점근선",
    "6. 일반형",
    "7. 표준형"
]

# 퀴즈 개념 선택
selected_quiz_option = st.selectbox(
    "퀴즈를 풀 개념을 선택하세요.",
    options=quiz_options,
    key="quiz_select_key"
)

# 선택된 옵션에서 개념 이름만 추출
selected_concept = selected_quiz_option.split(". ")[1]
quiz_data = QUIZ_QUESTIONS.get(selected_concept)

if quiz_data:
    st.subheader(f"❓ 문제: {selected_concept}")
    # 문제 출력
    st.markdown(f"**질문:** {quiz_data['question']}")

    # 사용자 답변 입력
    user_answer = st.radio(
        "O 또는 X를 선택하세요.",
        options=['O', 'X'],
        key="user_answer_key"
    )

    # 정답 확인 버튼
    if st.button("정답 확인!"):
        is_correct = (user_answer == quiz_data['correct_choice'])
        
        st.markdown("---")
        if is_correct:
            st.balloons()
            st.success(f"🎉 **정답입니다!** (선택: {user_answer})")
        else:
            st.error(f"❌ **아쉽지만 오답입니다.** (선택: {user_answer})")

        # 해설 출력
        st.subheader("📝 해설")
        st.markdown(f"**정답:** {quiz_data['correct_choice']}")
        st.markdown(quiz_data['explanation'])

st.markdown("---")
st.info("더 깊은 학습을 원한다면 1번 섹션에서 개념을 다시 살펴보세요!")
