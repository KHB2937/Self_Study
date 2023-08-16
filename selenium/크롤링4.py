from bs4 import BeautifulSoup

doc = open("./test3.html", encoding="utf-8") # 로컬에 있는 test1.html 파일을 블러와라
bs = BeautifulSoup(doc, "lxml")

ulList = bs.find_all("ul")
liList = ulList[0]
for li in liList:
    print(li.text)

print("과일----------")
liList = ulList[1]
for li in liList:
    print(li.text)