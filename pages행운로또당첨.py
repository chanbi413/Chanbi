import streamlit as st
import random

# --- 앱 설정 ---
st.set_page_config(
    page_title="랜덤 숫자 조합 생성기",
    layout="centered"
)

# 배경 이미지 설정 함수 (네잎클로버 이미지 사용)
def set_background_image():
    # 이 부분은 로컬 파일 경로 대신, 온라인에서 접근 가능한 이미지 URL을 사용하거나 
    # Streamlit의 정적 폴더에 이미지를 저장해야 합니다.
    # 안전을 위해 로컬 파일 경로는 주석 처리하고, CSS 스타일로 배경을 설정합니다.
    
    # 네잎클로버 이미지를 연상시키는 배경색과 스타일을 사용합니다.
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #e0f2e0; /* 연한 녹색 배경 */
            background-image: url('https://user-images.githubusercontent.com/83011380/215749718-4a6c8413-a749-41e9-9069-3a3c990b7a8d.png'); /* 일반적인 클로버 패턴 이미지 URL을 사용할 수 있으나, 여기서는 안전을 위해 일반 배경색으로 대체 */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            padding: 20px;
        }
        .main-header {
            color: #006400; /* 진한 녹색 제목 */
            font-weight: bold;
            text-align: center;
        }
        .result-box {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .number-display {
            display: inline-block;
            background-color: #4CAF50; /* 녹색 공 */
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            line-height: 40px;
            text-align: center;
            margin: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- 메인 함수 ---
def main():
    set_background_image()
    
    st.markdown("<h1 class='main-header'>✨ 랜덤 숫자 조합 생성기 ✨</h1>", unsafe_allow_html=True)
    st.write("1부터 45 사이의 숫자 중 6개의 숫자를 무작위로 생성합니다.")

    # 1. 게임 수 입력 받기 (슬라이더 사용)
    num_games = st.slider(
        '생성할 조합 개수 (1~10)',
        min_value=1,
        max_value=10,
        value=1
    )

    st.markdown("---")

    # 2. '생성' 버튼
    if st.button('✨ 조합 생성 ✨'):
        st.subheader(f"{num_games}개의 무작위 숫자 조합:")
        
        # 3. 입력된 횟수만큼 숫자 조합 생성
        for i in range(1, num_games + 1):
            # 1부터 45 사이의 숫자 중 6개를 중복 없이 무작위로 선택
            numbers = random.sample(range(1, 46), 6)
            numbers.sort() # 보기 좋게 숫자를 오름차순으로 정렬
            
            # 결과 표시
            st.markdown(f"<div class='result-box'>", unsafe_allow_html=True)
            st.markdown(f"**게임 {i}:**", unsafe_allow_html=True)
            
            # 각 숫자를 동그란 공 모양으로 표시
            number_html = "".join([f"<span class='number-display'>{num}</span>" for num in numbers])
            st.markdown(f"<div>{number_html}</div>", unsafe_allow_html=True)
            
            st.markdown(f"</div>", unsafe_allow_
