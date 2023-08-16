url = "https://hades-cerberus.v.kakao.com/charon/channel_home_ranking_latest?size=5&consumerId=media&cpId=94&hours=3"
# 파이썬이 정보를 함수하고 주고받을때 클래스를 잘 안만들고 왠만하면 Dict타입이나 tuple타입에 담아 보낸다.
# 브라우저 www.daum.net -> daum서버로 정보를 보낼때 get방식, header라는 구조를 먼저 보낸다.

custom_header = {
    "referer":"https://hades-cerberus.v.kakao.com",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

from bs4 import BeautifulSoup   # html 문서를 파싱하는 라이브러리
import requests                 # 원격으로 서버에 요청해서 html 문서를 받아오는 라이브러리
import json                     # json 데이터를 => dict타입으로 전환
                                # restful api 서버가 클라이언트와 서버간에 json형식의 데이터를 주고받는게 목적임

# requests 객체에 함수가 get, post도 있다. get으로 보낼지 post로 보낼지는 웹서버의 설정방식에 따라 다르다
response = requests.get(url, headers=custom_header) # 서버로 요청을 보내고 응답을 받는다
print(response.status_code) # 200일때 성공이다
if response.status_code!=200: #에러임
    print("error", response.status_code)
    exit()

data = response.content
print(type(data)) #byte배열
data = json.loads(data)
print(type(data))

dataList = data["body"]["data"]
for data in dataList:
    print("title")
    print(data["title"])
    print("summary")
    print(data["summary"])

    writers = data["writers"]
    for writer in writers:
        print(writer["name"], writer["email"])