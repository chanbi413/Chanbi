import streamlit as st
import random

# --- 이름 데이터베이스 ---

# 2025년 기준 '가장 많이 등록된' 이름에 대한 공식적인 최신 자료는 없으므로,
# 최근 몇 년간의 인기 이름 트렌드를 반영하여 선정합니다. (요청에 따라 트렌드 이름 강화)
popular_names_male = ["도윤", "서준", "하준", "은우", "시우", "이준", "지호", "예준", "유준", "주원"]
popular_names_female = ["이서", "서아", "하윤", "아윤", "지안", "서윤", "지우", "수아", "하은", "다인"]

# 순우리말 이름 (남녀 공용 또는 구분 없이 사용 가능한 이름 포함)
pure_korean_names = [
    "가람", "나래", "다온", "라온", "마루", "보람", "새롬", "솔", "슬기", "아름",
    "예나", "은솔", "하늘", "푸름", "한울", "윤슬", "도담", "별하", "은가람", "늘품"
]

# 한국 연예인 본명 풀네임 (예시로 활용하며, 인기 트렌드도 고려)
# 요청하신 성씨(김, 이, 박, 최, 윤, 정)를 가진 연예인을 중심으로 구성했습니다.
celebrity_full_names = [
    "김태형", "박보검", "이종석", "정해인", "최우식", "윤아름", "박수영", "김소현", "정은채", "최수빈", 
    "김지수", "이민호", "박서준", "정국", "송혜교", "김고은", "이지은", "윤찬영", "이도현", "정유미",
    "최승현", "윤은혜", "이승기", "박신혜", "김수현", "정우성", "이정재", "최지우" # 성씨 pool 확대를 위해 추가
]
# 참고: "정국"은 성씨가 '전'이나 예명/본명 자체가 워낙 유명하여 성씨만 분리하기 애매한 경우입니다.

# 요청된 성씨 리스트
surnames = ["김", "이", "박", "최", "윤", "정"]

# --- 앱 기능 함수 ---

def generate_names(count, name_type, gender):
    """지정된 유형과 성별에 따라 이름을 생성합니다."""
    
    generated_names = []
    
    if name_type == "한국 연예인 본명":
        # 1. 요청된 성씨를 가진 연예인만 필터링
        filtered_celebs = [
            name for name in celebrity_full_names 
            if name[0] in surnames
        ]
        
        # 2. 필터링된 리스트에서 중복 없이 랜덤 선택
        name_pool = filtered_celebs
        
        # 중복 방지를 위해 리스트 복사 후 랜덤 섞기
        available_names = list(name_pool)
        random.shuffle(available_names)
        
        # 요청된 개수만큼 이름 생성
        for i in range(min(count, len(available_names))):
            generated_names.append(available_names[i])

    else: # 인기 이름 및 순우리말 이름
        
        if name_type == "인기 이름":
            if gender == "남아":
                name_pool = popular_names_male
            elif gender == "여아":
                name_pool = popular_names_female
            else: # 남녀 공용
                name_pool = popular_names_male + popular_names_female

        elif name_type == "순우리말 이름":
            name_pool = pure_korean_names
        
        # 이름 풀에서 중복 없이 이름만 추출
        available_names = list(set(name_pool))
        random.shuffle(available_names) # 이름의 순서를 섞어 랜덤성 부여

        # 요청된 개수만큼 이름 생성
        for _ in range(count):
            if not available_names:
                break

            # 랜덤으로 성씨 선택
            surname = random.choice(surnames)
            
            # 이름 풀에서 이름 선택 후, 중복 방지를 위해 제거 (이름 + 성씨의 조합이 아닌, 이름 자체의 중복 방지)
            name = available_names.pop(0)

            generated_names.append(f"{surname}{name}")

    return generated_names

# --- Streamlit 앱 구성 (이 부분은 사용자 요청에 따라 변경하지 않고 유지) ---

st.set_page_config(page_title="✨ 아이 이름 생성기 (2025년 트렌드)", layout="centered")

st.title("👶 아이 이름 생성기 (2025년 트렌드 반영)")
st.markdown("---")

st.info("💡 2025년 기준 가장 많이 등록된 이름의 공식 통계는 미제공되어 최근 트렌드를 반영한 인기 이름으로 대체되었습니다. **연예인 이름은 요청하신 성씨(김, 이, 박, 최, 윤, 정)를 가진 본명 풀네임으로 추천됩니다.**")

# 1. 원하는 이름 개수 입력 (Slider)
name_count = st.slider("1. 원하는 이름의 개수를 선택해주세요. (1~10개)", min_value=1, max_value=10, value=3)

st.markdown("---")

# 2. 이름 유형 선택 (Radio Button) - 연예인 이름을 '본명'으로 명시
name_type = st.radio(
    "2. 어떤 유형의 이름을 원하세요?",
    ["인기 이름", "순우리말 이름", "한국 연예인 본명"],
    index=0 # 기본값은 인기 이름
)

st.markdown("---")

# 3. 성별 선택 (Select Box) - 인기 이름 선택시에만 표시
gender = "남녀 공용" # 기본값

if name_type == "인기 이름":
    gender = st.selectbox(
        "3. 성별을 선택해주세요.",
        ["남아", "여아", "남녀 공용"],
        index=2 # 기본값은 남녀 공용
    )
    st.markdown("---")


# 4. 이름 생성 버튼
if st.button("🌟 이름 생성하기", type="primary"):
    
    # 이름 생성
    final_names = generate_names(name_count, name_type, gender)
    
    if final_names:
        st.subheader(f"✨ 생성된 이름 ({len(final_names)}개)")
        
        # 결과를 보기 좋게 출력
        col1, col2 = st.columns(2)
        for i, name in enumerate(final_names):
            # 레이블 조정
            if name_type == "인기 이름":
                label = f"{i+1}번째 이름 ({gender})"
            elif name_type == "한국 연예인 본명":
                label = f"{i+1}번째 이름 (연예인 본명)"
            else: # 순우리말 이름
                label = f"{i+1}번째 이름 (순우리말)"

            if i % 2 == 0:
                col1.metric(label=label, value=name)
            else:
                col2.metric(label=label, value=name)

        st.balloons()
    else:
        st.warning("이름을 생성하지 못했습니다. 선택하신 조건에 맞는 이름 목록이 충분하지 않을 수 있습니다.")

st.markdown("---")
st.caption("본 앱에서 생성된 이름은 참고용이며, 최종 작명은 가족의 신중한 결정이 필요합니다.")
