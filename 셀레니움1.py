# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# #브라우저 꺼짐 방지 옵션
# chrome_options = Options()
# # chrome_options.add_experimental_option("datach", True)
# chrome_options.add_argument('--user-data-dir=C:/하둡/PY_workespace/dataset')  # 사용자 프로필 경로 지정
# # 저장 경로 설정 예: C:/Users/Username/AppData/Local/Google/Chrome/User Data

# #find_element
# #By.NAME - input태그의 name속성으로 검색해라   name 속성이 q이다.
# #input, select, textarea 까지 전부 name속성이 있다
# # driver.find_element(By.XPATH, '//button[text()="Some text"]')
# # driver.find_element(By.XPATH, '//button')
# # driver.find_element(By.ID, 'loginForm')
# # driver.find_element(By.LINK_TEXT, 'Continue')
# # driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
# # driver.find_element(By.NAME, 'username')
# # driver.find_element(By.TAG_NAME, 'h1')
# # driver.find_element(By.CLASS_NAME, 'content')
# # driver.find_element(By.CSS_SELECTOR, 'p.content')
# # driver.find_elements(By.ID, 'loginForm')
# # driver.find_elements(By.CLASS_NAME, 'content')
# #

# #requests 라이브러리는 문서만 불러오고 끝난다.
# #driver 크롬브라우저 자체다
# driver = webdriver.Chrome(options=chrome_options) # webdriver객체에 드라이버 파일이 있는곳을 알려준다.
# driver.get("https://google.com")

# #find_element
# #By.NAME - input태그의 name속성으로 검색해라 name 속성이 q이다.
# #input, select, textarea 까지 전부 name속성이 있다
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("파이썬") #input박스에 검색어를 넣는다
# search_box.submit() # 서버로 전송한다.

import selenium

print(selenium.__version__)
