import requests #html문서를 원격으로 가져옴

# 문서를 읽어와서 상태정보를 response 객체로 빈환한다.
# response = requests.get("가져올문서명")
response = requests.get("https://www.yna.co.kr/view/AKR20230627031700530?input=1195m")
print(response.status_code) # 상태코드, 사이트가 없거나 문서가 없거나
                            # 가져올수 없을때 상태정보가 저장된다
                            # 200 - ok http프로토콜에서 문서가 제대로 왔다 200

if response.status_code!=200:
    print("error")
    exit()

from bs4 import BeautifulSoup
bs = BeautifulSoup(response.content, "lxml")

h3 = bs.find("h1")
print(h3.text)

div = bs.find("div", {"class":"content01"})
print(div.text)
# div = bs.find("div", {"class":"comp-box photo-group"})
# print(div)
# print("----------------------------------------")
# div = bs.find("div", {"id":"newsWriterCarousel01"})
# print(div)
