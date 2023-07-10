import re
import pandas as pd
import gdown
import streamlit as st

# 데이터 프레임 가져오기
def get_dataframe():
    # 구글 드라이브 공유 링크에서 파일 ID 추출
    link = 'https://drive.google.com/file/d/1-YNWYdFPYOYU4fjSLnSpCicvNIPPmKS7/view?usp=drive_link'
    file_id = re.findall(r'/d/([a-zA-Z0-9_-]+)', link)[0]

    # 파일 다운로드
    url = f'https://drive.google.com/uc?id={file_id}'
    output_file = '전국음식점(수정본).csv'  # 저장할 파일 이름을 지정합니다.
    gdown.download(url, output_file)

    # 데이터프레임 로드
    df = pd.read_csv(output_file)
    return df

# 사용자 입력 받기
def get_user_input(df):
    # 지역 선택
    regions = df['소재지전체주소'].unique().tolist()
    selected_region = st.sidebar.selectbox('소재지전체주소', regions)

    # 업태구분명 선택
    categories = df['업태구분명'].unique().tolist()
    selected_category = st.sidebar.selectbox('업태구분명 선택', categories)

    return selected_region, selected_category

# 데이터 프레임 필터링
def filter_dataframe(df, region, category):
    filtered_df = df[(df['소재지전체주소'] == region) & (df['업태구분명'] == category)]
    return filtered_df

# streamlit 앱
def main():
    # 데이터프레임을 가져옴
    df = get_dataframe()

    # 사용자 입력 받기
    selected_region, selected_category = get_user_input(df)

    # 데이터 프레임 필터링
    filtered_df = filter_dataframe(df, selected_region, selected_category)

    # 선택된 부분만 데이터프레임으로 출력
    st.write(filtered_df)

if __name__ == '__main__':
    main()