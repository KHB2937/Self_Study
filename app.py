# main.py
import streamlit as st
import pandas as pd
import gdown


# 데이터프레임을 가져오는 함수
def get_dataframe():
    # 구글 드라이브 공유 링크에서 파일 ID 추출
    file_id = 'https://drive.google.com/file/d/1-YNWYdFPYOYU4fjSLnSpCicvNIPPmKS7/view?usp=drive_link'  # 구글 드라이브 공유 링크에서 추출한 파일 ID를 입력합니다.

    # 파일 다운로드
    url = f'https://drive.google.com/uc?id={file_id}'
    output_file = '전국음식점(수정본).csv'  # 저장할 파일 이름을 지정합니다.
    gdown.download(url, output_file)

    # 데이터프레임 로드
    df = pd.read_csv(output_file)
    return df

# streamlit 앱
def main():
    # 데이터프레임을 가져옴
    df = get_dataframe()

    # 데이터프레임 출력
    st.write(df)
