url = "https://hades-proxy.v.daum.net/toros/query/mediadaum/soonsal_v2?body=%7B%22itemid%22%3A%2220230627174712587%22%2C%22category%22%3A%22news%22%7D"


custom_header = {
    "referer":"https://hades-proxy.v.daum.net",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

from bs4 import BeautifulSoup
import requests
import json

response = requests.get(url, headers=custom_header)
print(response.status_code)
if response.status_code != 200:
    print("error", response.status_code)
    exit()

data = response.content
print(type(data))#byte배열
data = json.loads(data) #dict타입
print(type(data))

resultList = data["results"]
for result in resultList:
    print(result["title"])