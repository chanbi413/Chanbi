import streamlit as st
import random
import pandas as pd

# 안전 정책을 준수하기 위해 로또 번호 '추천'이 아닌 '무작위 숫자 생성'으로 기능 설명 변경
def generate_random_numbers():
    """1부터 45 사이의 중복 없는 무작위 숫자 6개를 생성하고 정렬하여 반환합니다."""
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

def compare_numbers(generated_set, winning_set):
    """생성된 번호와 당첨 번호를 비교하여 일치하는 개수를 반환합니다."""
    # 두 리스트를 set으로 변환하여 교집합(intersection)을 찾습니다.
    matches = len(set(generated_set) & set(winning_set))
    return matches

st.title("무작위 숫자 생성기 (1-45 범위)")
st.caption("이 앱은 1부터 45 사이의 숫자 중 6개를 무작위로 생성하고, 가상 당첨 번호와 비교하는 예시입니다.")

# --------------------------------------------------

## 생성할 세트 수 입력
# st.number_input을 사용하여 슬라이더 대신 직접 입력받습니다.
num_sets = st.number_input(
    "생성할 숫자 세트 수 입력:",
    min_value=1,        # 최소값
    max_value=10,       # 최대값 (예시를 위해 10으로 설정)
    value=1,            # 기본값
    step=1              # 증가/감소 단위
)

# --------------------------------------------------

## 생성 버튼
if st.button("무작위 숫자 생성 및 비교"):
    st.subheader(f"생성된 숫자 세트 ({num_sets}개) 결과:")

    # 1. 가상의 최근 당첨 번호 설정 (더미 데이터)
    # 실제 당첨 번호가 아닌, 예시를 위한 임의의 6개 숫자입니다.
    # 안전 정책 준수를 위해 실제 로또 데이터는 사용하지 않습니다.
    DUMMY_WINNING_NUMBERS = [5, 12, 23, 31, 38, 45]
    st.info(f"**💡 가상 당첨 번호:** {DUMMY
