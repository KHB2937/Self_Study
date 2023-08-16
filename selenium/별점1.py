# 필요한 모듈들을 불러옵니다
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

# 크롬 드라이버 생성
driver = webdriver.Chrome()
driver.implicitly_wait(3) # 웹사이트 로딩 대기시간


# 데이터 프레임 생성
columns = ['별점']
data = []

# 사이트 접속하기
driver.get('https://www.naver.com/')
search_box = driver.find_element(By.NAME, 'query')

# 검색어 입력하기
search_term = "부천 맛집"
search_box.send_keys(search_term)

# 검색창에서 Enter 키 누르기
search_box.send_keys(Keys.RETURN)

# 결과 페이지를 로드하는데 시간이 걸릴 수 있으므로 잠시 대기
time.sleep(3)

# 첫 번째 검색 결과의 링크를 클릭합니다.
first_result_link = driver.find_element(By.XPATH, "//ul[@class='lst_type lst_type_v2']//a")
first_result_link.click()

time.sleep(3)

# 드라이버로 현재 윈도우를 변경합니다.
driver.switch_to.window(driver.window_handles[-1]) #이거 없으면 안되더라..

# 특정 XPath를 가진 a 태그를 찾아 클릭하기
link = driver.find_element(By.XPATH, "//a[@role='tab' and contains(@class, '_tab-menu') and contains(@href, '/review')]//span")
link.click()
time.sleep(3)

# "더보기" 버튼 클릭하여 리뷰를 가져옵니다.
while True:
    try:
        # 더보기 버튼 클릭
        more_button = driver.find_element(By.XPATH, "//a[contains(@class, 'fvwqf')]")
        more_button.click()
        time.sleep(2)
    except:
        # 더 이상 더보기 버튼이 없으면 반복문 종료
        break

#리뷰 받아오기
review_elements = driver.find_elements(By.XPATH, "//ul[@class='eCPGL']//li[contains(@class, 'YeINN')]")

# 리뷰 출력하기
for i, review in enumerate(review_elements):
    print(f"리뷰 {i+1}:")
    
    # # 리뷰 작성자
    # reviewer = review.find_element(By.XPATH, ".//div[@class='sBWyy']").text
    # print(f"작성자: {reviewer}")

    # # 리뷰 내용
    # content_elements = review.find_elements(By.XPATH, ".//span[@class='zPfVt']")

    # if len(content_elements) > 0:
    #     content = content_elements[0].text
    # else:
    #     content = 'nan'

    # print(f"내용: {content}\n")

    # 별점 변수를 None으로 초기화합니다.
    rating = None

    try:
        # 리뷰에서 별점 요소를 찾습니다.
        rating_element = review.find_element(By.XPATH, ".//div[contains(@class, 'gyAGI')]")
    
        # 새로운 구조를 확인하여 더 적합한 접근을 시도합니다.
        try:
            rating = rating_element.find_element(By.XPATH, ".//span[contains(@class, 'P1zUJ HNG_1')]/em").text
        except NoSuchElementException:
            # 별점 정보를 찾지 못한 경우, 기존 구조의 별점 값을 찾습니다.
            rating = rating_element.text

    except NoSuchElementException:
        # 별점 정보를 찾지 못한 경우, 별점 값을 'NaN'으로 설정합니다.
        rating = 'NaN'

    # # 별점 값을 출력합니다.
    # print(f"별점: {rating}")

    # 크롤링한 데이터를 data 리스트에 추가
    data.append([rating])

# 데이터프레임으로 변환
df = pd.DataFrame(data, columns=columns)
print(df)

# CSV 파일로 저장
csv_file = "C:/py/star.csv"
df.to_csv(csv_file, index=False, encoding="utf-8-sig")

# CSV 파일 읽기 (UTF-8 인코딩으로 지정)
df_read = pd.read_csv(csv_file, encoding="utf-8")
print(df_read)

# 프로그램을 종료하려면 사용자의 입력을 기다립니다.
input("Press Enter to exit...")