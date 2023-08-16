import requests #html문서를 원격으로 가져옴

# 문서를 읽어와서 상태정보를 response 객체로 빈환한다.
# response = requests.get("가져올문서명")
response = requests.get("https://www.en-core.com/")
print(response.status_code) # 상태코드, 사이트가 없거나 문서가 없거나
                            # 가져올수 없을때 상태정보가 저장된다
                            # 200 - ok http프로토콜에서 문서가 제대로 왔다 200

if response.status_code!=200:
    print("error")
    exit()

from bs4 import BeautifulSoup
bs = BeautifulSoup(response.content, "lxml")

ul = bs.find("ul", {"id":"wrap"})
liList = ul.find_all("li")
for li in liList:
    div = li.find("div", {"class":"con"})
    strong = div.find("strong")
    print(strong.text)