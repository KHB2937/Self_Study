from bs4 import BeautifulSoup  #html 문서를 파싱하는 라이브러리
import requests
import pandas as pd
#html문서는 그냥 불러와도 된다
response = requests.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do")
if response.status_code!=200:
    print("Error", response.status_code)
    exit()
#print( response.content )
content = response.content
bs = BeautifulSoup(content) #json.loads 처럼 BeautifulSoup 객체를 만들어서 파싱이 된다
table = bs.find("table", {"id": "weather_table"})
tbody = table.find("tbody")  # 수정: tbody 태그를 찾습니다
trList = tbody.find_all("tr")  # tr 태그의 모든 정보를 가져옵니다

# data = []  # 데이터를 저장할 리스트 생성

# for tr in trList:
#     tdList = tr.find_all("td")
#     row = [td.text for td in tdList]  # 각 행의 데이터를 리스트로 저장
#     data.append(row)

# # 데이터 프레임 생성
# df = pd.DataFrame(data)

# print(df)

df = pd.DataFrame()

for tr in trList:
    #print(tr)
    td = tr.find_all("td")
    data={"location":td[0].text, "A":td[5].text, "B":td[6].text, "C":td[7].text}
    df = df.append(data, ignore_index=True)

print(df)
# 파일에 저장시 index 저장 안하고 excel에서 볼 수 있도록 cp949
df.to_csv("기상정보.csv", index=False, encoding="CP949")    