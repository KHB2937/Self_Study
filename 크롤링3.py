from bs4 import BeautifulSoup

doc = open("./test2.html", encoding="utf-8") # 로컬에 있는 test1.html 파일을 블러와라
bs = BeautifulSoup(doc, "lxml")

#1.table태그에 대한 참조를 가져온다
#2.tbody 나 thead에 대한 참조를 가져온다(생략가능)
#3. tr태그에 대한 참조를 가져온다

table = bs.find("table")
thead = table.find("thead")
tr = thead.find("tr")
th = tr.find_all("th")
for t in th:
    print(t.text)


#tbody
tbody = table.find("tbody")
trList = tbody.find_all("tr")
for tr in trList:
    tdList = tr.find_all("td")
    for td in tdList:
        print(td.text, end=' ')
    print()