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

def get_concept_summary(concept_name: str, length: int) -> str:
    """
    사용자가 요청한 개념에 대한 설명을 가져오고, 지정된 줄 수로 요약(시뮬레이션)합니다.
    """
    if concept_name not in CONCEPT_EXPLANATIONS:
        # 개념이 없을 경우 에러 메시지 반환
        return f"죄송합니다. **{concept_name}**에 대한 개념 설명은 준비되어 있지 않습니다. '유리함수', '정의역', '치역', '일반형', '표준형' 중 하나를 입력해 주세요."

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

st.title("📚 유리함수 개념 학습 도우미")
st.markdown("---")

# 전체 개념 소개
st.header("✨ 유리함수의 핵심 개념")
st.markdown(
    "유리함수는 분수 꼴로 나타나는 함수이며, **정의역, 치역, 점근선** 이해가 필수입니다. "
    "함수의 형태에 따라 **일반형**과 **표준형**으로 구분됩니다. "
    "아래 입력창에 알고 싶은 개념을 입력하고, 원하는 설명 길이를 설정해 보세요."
)
st.markdown("---")

# 사용자 입력 및 슬라이더
col1, col2 = st.columns([2, 1])

with col1:
    # 텍스트 입력창
    concept_input = st.text_input(
        "궁금한 개념을 입력하세요 (예: 정의역, 표준형, 유리함수)",
        value="유리함수",
        key="concept_input_key"
    ).strip() # 앞뒤 공백 제거

with col2:
    # 설명 길이 슬라이드바
    # 최대 내용 길이(3줄)에 맞춰 max_value와 value를 3으로 설정
    summary_length = st.slider(
        "설명 글의 길이 설정 (줄 수)",
        min_value=1,
        max_value=3, # 최대값 3으로 수정
        value=3, # 기본값 3으로 설정
        step=1,
        key="summary_length_key"
    )

st.markdown("---")

# 결과 출력 영역
st.header(f"🔍 개념 설명: {concept_input if concept_input else '개념을 입력해 주세요'}")

if concept_input:
    # 개념 설명 함수 호출
    explanation = get_concept_summary(concept_input, summary_length)
    
    # Markdown으로 결과 출력
    st.markdown(explanation)
    
    # 입력된 개념이 유효할 경우, 수식 렌더링을 위해 st.latex를 사용
    if concept_input in ["유리함수", "일반형", "표준형"]:
        st.subheader("💡 관련 수학 공식")
        if concept_input == "유리함수":
            st.latex("y = \\frac{P(x)}{Q(x)}, \\quad (Q(x) \\neq 0)")
        elif concept_input == "일반형":
            st.latex("y = \\frac{ax+b}{cx+d} \\quad \\rightarrow \\quad (c \\neq 0, ad-bc \\neq 0)")
        elif concept_input == "표준형":
            st.latex("y = \\frac{k}{x-p} + q")

st.markdown("---")
st.info("개념 입력창에 '유리함수', '정의역', '치역', '일반형', '표준형'을 입력해 보세요.")
