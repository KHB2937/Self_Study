# 필요한 모듈들을 불러옵니다
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


# 크롬 드라이버 생성
driver = webdriver.Chrome()
driver.implicitly_wait(3) # 웹사이트 로딩 대기시간

# 웹 페이지로 이동
driver.get("https://map.naver.com")
time.sleep(3)

# 검색어 입력란 요소 찾기
search_input = driver.find_element(By.CSS_SELECTOR, 'input.input_search')
time.sleep(1)

# 검색어 입력
search_term = "부천 맛집"
search_input.send_keys(search_term)
time.sleep(2)
# 검색어 입력 후 엔터 키 입력
search_input.send_keys(Keys.ENTER)
time.sleep(5)

# iframe으로 전환
iframe_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchIframe')))
driver.switch_to.frame(iframe_element)

# 요소 찾기
ul_element = driver.find_element(By.TAG_NAME, 'ul')
li_element = ul_element.find_element(By.XPATH, './/li[1]')
div_element = li_element.find_element(By.XPATH, './/div')
a_element = div_element.find_element(By.XPATH, './/a')

# 요소 클릭
a_element.click()
time.sleep(3)

# iframe에서 벗어나기
driver.switch_to.default_content()

# iframe으로 전환
iframe_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'entryIframe')))
driver.switch_to.frame(iframe_element)

#가게명
span_element = driver.find_element(By.XPATH, '//*[@id="_title"]/span[1]')
name = span_element.text

# 주소
span_element = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/div/div[1]/div/a/span[1]')
address = span_element.text

#전화번호
span_element = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/div/div[4]/div/span[1]')
number = span_element.text

# 별점
try:
    star_element = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[1]/em')
    star = star_element.text
except NoSuchElementException:
    star = 'NaN'

review_element = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[5]/span')
review_element.click()
time.sleep(2)
try:
    reviNum_element = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div:nth-child(7) > div:nth-child(2) > div:nth-child(3) > h2 > span.place_section_count')
    reviNum = reviNum_element.text
except NoSuchElementException:
    review = 'NaN'



# 텍스트 출력
print(name)
print(address)
print(number)
print(star)
print(review)
print('-------------------')

# 프로그램을 종료하려면 사용자의 입력을 기다립니다.
input("Press Enter to exit...")
