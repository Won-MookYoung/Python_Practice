import requests
from bs4 import BeautifulSoup
#헤더옵션
header = {'User-Agent':'Mozila/5.0'}
response= requests.get('https://n.news.naver.com/mnews/article/003/0011282908?sid=101',headers=header)

html=response.text
soup=BeautifulSoup(html,'html.parser')

title=soup.select_one('.media_end_head_title')
print(title.text)

## 에러가 남 요청을 주고 못받아오는듯 
### 거절당했다~~
### 헤더설정하면됨l