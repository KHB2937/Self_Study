# 로컬에 있는 문서를 불러온다

from bs4 import BeautifulSoup

doc = open("./test1.html", encoding="utf-8") # 로컬에 있는 test1.html 파일을 블러와라
bs = BeautifulSoup(doc, "lxml")
# 문서를 읽자마자 tree구조로 dom구조를 읽는다
h1 = bs.find("h1") # find함수는 무조건 첫번째거 하나만 가져온다
print(h1)
print(h1.text)

h1List = bs.find_all("h1")
print(h1List[0].text)
print(h1List[1].text)

print("-----------all-----------")
for h1 in h1List:
    print(h1.text)


print("-----------id로 파싱하기-----------")
h1 = bs.find("h1", {"id":"title1"})
print(h1)

h1 = bs.find("h1", id = "title2")
print(h1)


print("-----------class로 파싱하기-----------")
h1 = bs.find("h1", {"class":"title3"})
print(h1)

h1 = bs.find("h1", class_="title4")
print(h1)

print("속성과 배열을 ----------")
h1List = bs.findAll("h1", {"class":"title3"}) # find_all과 사용법이 같다
for h1 in h1List:
    print(h1.text)