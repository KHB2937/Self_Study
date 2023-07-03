import requests #html문서를 원격으로 가져옴

# 문서를 읽어와서 상태정보를 response 객체로 빈환한다.
# response = requests.get("가져올문서명")
response = requests.get("https://www.python.org/")
print(response.status_code) # 상태코드, 사이트가 없거나 문서가 없거나
                            # 가져올수 없을때 상태정보가 저장된다
                            # 200 - ok http프로토콜에서 문서가 제대로 왔다 200

if response.status_code==200:
    # print(response.content)
    pass
else:
    print("fail")

    # BeautifulSoup -- html문서로부터 내가 원하는 데이터만 추출한다.
    #              -- ajax로 기술된 문서는 가져오는 방식이 다르다
    # 
    # BeautifulSoup - 이 클래스는 html문서를 파싱한다.
    # 이 문서 자체는 원격에서 가져오던 로컬에 있는 문서든 상관이 없다.
    # html을 가져와서 분석할 수도 있고 로컬에 있는 문서를 읽어와서 파싱할 수도 있다.
    # 파싱 : html 또는 xml, json, txt등의 문서에서 원하는 내용을 가져오는 동작을 말한다
    # 파서 : 파싱을 하는 프로그램
    from bs4 import BeautifulSoup
    bs = BeautifulSoup(response.content, "lxml")
    # 문서를 주고
    # 출력하자
    print(bs.title)
    print(bs.title.text) 
                            # 단일태그일때랑, 배열태그일때, id는 class를 이용해
                            # 데이터를 추출하게 된다.
