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




# 프로그램을 종료하려면 사용자의 입력을 기다립니다.
input("Press Enter to exit...")