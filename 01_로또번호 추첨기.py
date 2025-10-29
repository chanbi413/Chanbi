import streamlit as st
import random

# 안전 정책을 준수하기 위해 로또 번호 '추천'이 아닌 '무작위 숫자 생성'으로 기능 설명 변경
def generate_random_numbers():
    """1부터 45 사이의 중복 없는 무작위 숫자 6개를 생성합니다."""
    # 1부터 45까지의 범위에서 6개의 숫자를 무작위로 선택합니다.
    # sample 함수는 중복 없는 선택을 보장합니다.
    numbers = random.sample(range(1, 46), 6)
    # 숫자를 오름차순으로 정렬하여 반환합니다.
    numbers.sort()
    return numbers

st.title("무작위 숫자 생성기 (1-45 범위)")
st.caption("이 앱은 1부터 45 사이의 숫자 중 6개를 무작위로 생성하는 예시입니다.")

# --------------------------------------------------

## 생성할 세트 수 선택
# 최대 5세트까지만 허용하는 예시입니다.
num_sets = st.slider("생성할 숫자 세트 수 선택:", min_value=1, max_value=5, value=1)

# --------------------------------------------------

## 생성 버튼
if st.button("무작위 숫자 생성"):
    st.subheader(f"생성된 숫자 세트 ({num_sets}개):")
    
    # 선택된 세트 수만큼 숫자를 생성하고 표시
    for i in range(1, num_sets + 1):
        generated_numbers = generate_random_numbers()
        st.write(f"**세트 {i}:** {generated_numbers}")

# --------------------------------------------------

## 참고: Streamlit 사용법
# 이 코드를 'app.py' 등으로 저장한 후, 터미널에서 다음 명령어로 실행할 수 있습니다:
# streamlit run app.py
