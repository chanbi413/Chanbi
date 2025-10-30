import streamlit as st
import random
import time # 로딩 애니메이션을 위해 추가

# --- 앱 설정 ---
st.set_page_config(
    page_title="랜덤 숫자 조합 생성기",
    layout="centered",
    initial_sidebar_state="auto"
)

# 배경 이미지 및 스타일 설정 함수 (네잎클로버 이미지 연상)
def set_background_style():
    # 클로버 배경 스타일 (CSS)
    # 이미지는 GitHub Pages나 S3 등 온라인에서 접근 가능한 URL을 사용해야 스트림릿에서 안정적으로 표시됩니다.
    # 안전을 위해 일반적인 밝은 녹색 계열 배경과 클로버 패턴을 연상시키는 스타일을 적용합니다.
    st.markdown(
        """
        <style>
        .stApp {
            /* 연한 녹색 배경색 */
            background-color: #e0f8e0; 
            /* 클로버 패턴 대신 깔끔한 배경을 사용하거나, 사용자에게 클로버 패턴 URL을 넣도록 안내 */
            /* 예: background-image: url('YOUR_CLOVER_IMAGE_URL'); */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            padding-top: 20px;
        }
        .main-header {
            color: #006400; /* 진한 녹색 제목 */
            font-weight: 800;
            text-align: center;
            padding-bottom: 10px;
        }
        .result-box {
            background-color: rgba(255, 255, 255, 0.9);
            border: 2px solid #4CAF50; /* 클로버 색상 테두리 */
            border-radius: 12px;
            padding: 15px;
            margin-top: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            font-size: 18px;
        }
        .number-display {
            display: inline-block;
            background-color: #4CAF50; /* 녹색 공 (클로버) */
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            line-height: 45px;
            text-align: center;
            margin: 5px;
            box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
            animation: bounce 0.5s ease-in-out; /* 숫자 생성 시 애니메이션 추가 */
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- 메인 함수 ---
def main():
    set_background_style()
    
    st.markdown("<h1 class='main-header'>🍀 랜덤 숫자 조합 생성기 🍀</h1>", unsafe_allow_html=True)
    st.info("✨ 1부터 45 사이의 숫자 중 6개를 중복 없이 무작위로 선택합니다. ✨")

    # 1. 조합 개수 입력 받기 (1부터 10까지)
    num_games = st.slider(
        '생성할 조합 개수',
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )

    st.markdown("---")

    # 2. '생성' 버튼
    if st.button('🎲 조합 생성'):
        
        # 로딩 애니메이션
        with st.spinner('행운의 숫자를 고르는 중...'):
            time.sleep(1) # 잠시 멈춰서 애니메이션 효과를 줌

        st.subheader(f"✅ 생성된 {num_games}개의 무작위 조합:")
        
        # 3. 입력된 횟수만큼 숫자 조합 생성
        for i in range(1, num_games + 1):
            # 1부터 45 사이의 숫자 중 6개를 중복 없이 무작위로 선택
            # range(1, 46)은 1, 2, ..., 45를 의미
            numbers = random.sample(range(1, 46), 6)
            numbers.sort() # 보기 좋게 오름차순으로 정렬
            
            # 결과 표시
            st.markdown(f"<div class='result-box'>", unsafe_allow_html=True)
            st.markdown(f"**게임 {i}:**", unsafe_allow_html=True)
            
            # 각 숫자를 동그란 공 모양으로 표시
            number_html = "".join([f"<span class='number-display'>{num}</span>" for num in numbers])
            st.markdown(f"<div>{number_html}</div>", unsafe_allow_html=True)
            
            # 이 부분이 이전 질문에서 오류가 났던 부분입니다. 올바르게 수정되었습니다.
            st.markdown(f"</div>", unsafe_allow_html=True) 

# --- 앱 실행 ---
if __name__ == '__main__':
    main()
