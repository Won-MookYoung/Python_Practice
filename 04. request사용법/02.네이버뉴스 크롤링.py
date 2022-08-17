import requests
from bs4 import BeautifulSoup

response=requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
html=response.text


soup=BeautifulSoup(html,'html.parser')  #클래스로 만든객체
'''
#첫번째 기사의 제목
soup.select_one('.news_tit') # select one : 선택자와 매칭되는 첫번째 태그객체 반환
news_first=soup.select_one('.news_tit')
print(news_first.text)

#첫번째 기사의 본문
soup.select_one('.api_txt_lines.dsc_txt_wrap')
news_second=soup.select_one('.api_txt_lines.dsc_txt_wrap')   #클래스 두개 합칠떄 a.b
print(news_second.text)
'''
'''
# 1페이지 10개 기사 제목, 본문 크롤링 (select)
all=soup.select('.news_tit')   #셀렉트 : 선택자와 매칭되는 모든 태그객체를 리스트로 반환
for title in all:
    print(title.text)


soup.select('.api_txt_lines.dsc_txt_wrap')
con=soup.select('.api_txt_lines.dsc_txt_wrap')
for i in con:
    print(i.text)
'''
# asd=soup.select('.news_tit')
# zxc=soup.select('.api_txt_lines.dsc_txt_wrap')
# for i,j in zip(asd,zxc):
    # print(i.text)
    # print(j.text)

news =soup.select('.news_area')
for i in news:
    print(i.text)


# news=soup.select('.news_area')
# title_list=[]
# con_list=[]
# for x in news:
#     title_list.append([x])
# for y in news:
#     con_list.append([y])
# print(x)

### 기사 제목 한번에 출력하기 한페이지의 
n=1
new = soup.select('.news_area')
for i in new:
    print(n)
    print(i.select_one('.news_tit').text)
    print(i.select_one('.api_txt_lines.dsc_txt_wrap').text)
    n+=1
    

'''

news_list=soup.select('.news_area')
i=1
for news in news_list:
    #기사의 제목
    title=news.select_one('.news_tit')
    #본문
    content=news.select_one('.api_txt_lines.dsc_txt_wrap')
    print(i, title.text, content.text, sep='\n')
    i+=1
    '''