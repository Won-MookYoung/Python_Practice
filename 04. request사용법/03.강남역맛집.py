import requests
from bs4 import BeautifulSoup

response=requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EA%B0%95%EB%82%A8%EC%97%AD+%EB%A7%9B%EC%A7%91')
html=response.text

soup=BeautifulSoup(html,'html.parser')

delicious=soup.select('._3hn9q')
for i in delicious:
    title=delicious.select_one('.place_bluelink.OXiLu')

    print(title.text)