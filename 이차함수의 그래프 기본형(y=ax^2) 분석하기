import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 페이지 제목 설정
st.title('이차함수의 그래프 기본형($y=ax^2$) 분석하기')

st.markdown("""
이 앱을 통해 이차함수 $y=ax^2$의 계수 **$a$** 값의 변화에 따른 그래프의 모양을 관찰해 보세요.
""")

# ----------------------------------------

## ⚙️ 계수 $a$ 설정

# 사용자가 a 값을 조절할 수 있는 슬라이더 생성
# -10.0부터 10.0까지, 초기값은 1.0, 0.1 단위로 조절 가능.
# a가 0인 경우는 이차함수가 아니므로 (y=0) 제외하거나, 사용자가 0 근처의 값을 탐색할 수 있도록 0을 포함하지만 0에서는 함수가 직선이 됨을 고려해야 합니다.
# 여기서는 a가 0인 경우를 포함하여 사용자가 경계를 직접 확인할 수 있도록 설정합니다.
a = st.slider(
    '계수 $a$ 값 선택:',
    min_value=-10.0,
    max_value=10.0,
    value=1.0,
    step=0.1,
    format='%.1f' # 소수점 첫째 자리까지 표시
)

st.write(f'선택된 이차함수: $y = {a}x^2$')

# ----------------------------------------

## 📈 이차함수 그래프

# 그래프를 그리기 위한 데이터 생성
x = np.linspace(-5, 5, 400) # -5부터 5까지 x값 400개 생성
y = a * x**2 # 선택된 a 값에 따른 y 값 계산

# Matplotlib figure 생성
fig, ax = plt.subplots()

# 그래프 그리기
ax.plot(x, y, label=f'$y = {a}x^2$', color='blue')

# 축 및 그리드 설정
ax.axhline(0, color='gray', linestyle='--', linewidth=0.5) # x축 (y=0)
ax.axvline(0, color='gray', linestyle='--', linewidth=0.5) # y축 (x=0)
ax.grid(True, linestyle=':', alpha=0.6)

# 축 레이블 및 제목
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_title('이차함수 $y=ax^2$ 그래프')

# y축 범위 고정: a의 변화에 따른 폭 변화를 비교하기 쉽게 하기 위함
ax.set_ylim(-10, 10)
ax.set_xlim(-5, 5)

# 범례 표시
ax.legend()

# Streamlit에 그래프 출력
st.pyplot(fig)

# ----------------------------------------

## 💡 분석 결과 및 추론 가이드

st.header('추론 가이드')

# 1. 볼록성 분석 (a의 부호)
st.subheader('1. 그래프의 볼록성 (부호: $a$)')
if a > 0:
    st.success(f"**$a = {a}$ (양수)**: 그래프는 **아래로 볼록**합니다. (포물선이 위로 열려 있습니다.) 👇")
elif a < 0:
    st.error(f"**$a = {a}$ (음수)**: 그래프는 **위로 볼록**합니다. (포물선이 아래로 열려 있습니다.) 👆")
else:
    st.warning(f"**$a = {a}$ (0)**: $y=0$이므로, 그래프는 $x$축과 일치하는 직선입니다. 이차함수가 아닙니다.")

st.markdown("""
**귀납적 추론:**
* $a$가 양수일 때 ($a>0$) 그래프가 아래로 볼록한지 확인해 보세요.
* $a$가 음수
