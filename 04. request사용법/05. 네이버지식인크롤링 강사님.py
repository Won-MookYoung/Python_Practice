import requests
from bs4 import BeautifulSoup
'''
### 1단계 - 첫번쨰 질문의 제목 링크, 날짜, 설명
response = requests.get('https://kin.naver.com/search/list.naver?query=%EA%B3%A0%EC%96%91%EC%9D%B4')
html = response.text
soup=BeautifulSoup(html,'html.parser')

#링크태그
anchor=soup.select_one('._searchListTitleAnchor')  #dt >a 가능

#제목
title=anchor.text
#링크
link=anchor.attrs['href']
#날짜
date=soup.select_one('.txt_inline').text
#내용
content=soup.select_one('.txt_inline+dd').text #dd:nth-of-type(2) dd:nth-child(3) 가능

print(title, link, date, content, sep= '\n')
'''

'''
### 2단계 - 1페이지 전체 질문의 제목 링크, 날짜, 설명
response = requests.get('https://kin.naver.com/search/list.naver?query=%EA%B3%A0%EC%96%91%EC%9D%B4')
html = response.text
soup=BeautifulSoup(html,'html.parser')

# 1페이지 질문 10개 (태그객체)
lis = soup.select('.basic1>li')

i=1
for li in lis:
    #링크태그
    anchor=li.select_one('._searchListTitleAnchor')  #dt >a 가능
    #제목
    title=anchor.text
    #링크
    link=anchor.attrs['href']
    #날짜
    date=li.select_one('.txt_inline').text
    #내용
    content=li.select_one('.txt_inline+dd').text #dd:nth-of-type(2) dd:nth-child(3) 가능

    print(i, title, link, date, content, sep= '\n')
    i+=1
    '''

'''
### 3단계 - n페이지 까지 전체 질문의 제목 링크, 날짜, 설명
page = int(input(' 몇 페이지까지 크롤링할꺼?'))     # 사용자로부터입력받은 숫자

for p in range(1,page+1):

    response = requests.get(f'https://kin.naver.com/search/list.naver?query=%EA%B3%A0%EC%96%91%EC%9D%B4&page={p}')
    html = response.text
    soup=BeautifulSoup(html,'html.parser')

    # 1페이지 질문 10개 (태그객체)
    lis = soup.select('.basic1>li')
    i=1
    for li in lis:
        #링크태그
        anchor=li.select_one('._searchListTitleAnchor')  #dt >a 가능
        #제목
        title=anchor.text
        #링크
        link=anchor.attrs['href']
        #날짜
        date=li.select_one('.txt_inline').text
        #내용
        content=li.select_one('.txt_inline+dd').text #dd:nth-of-type(2) dd:nth-child(3) 가능

        print(i, title, link, date, content, sep= '\n')
        i+=1
        '''

'''
### 4단계 - 키워드 변경하고 n페이지 까지 전체 질문의 제목 링크, 날짜, 설명
keyword=input('검색어를 입력하세여 >>')
page = int(input('몇 페이지까지 크롤링할꺼?'))     # 사용자로부터입력받은 숫자

for p in range(1,page+1):

    response = requests.get(f'https://kin.naver.com/search/list.naver?query={keyword}&page={p}')
    html = response.text
    soup=BeautifulSoup(html,'html.parser')

    # 1페이지 질문 10개 (태그객체)
    lis = soup.select('.basic1>li')
    i=1
    for li in lis:
        #링크태그
        anchor=li.select_one('._searchListTitleAnchor')  #dt >a 가능
        #제목
        title=anchor.text
        #링크
        link=anchor.attrs['href']
        #날짜
        date=li.select_one('.txt_inline').text
        #내용
        content=li.select_one('.txt_inline+dd').text #dd:nth-of-type(2) dd:nth-child(3) 가능

        print(i, title, link, date, content, sep= '\n')
        i+=1
        '''


'''
### 5단계 - 엑셀 추가
import openpyxl
wb = openpyxl.Workbook()

# 엑셀 시트 선택
ws = wb.active

# 첫행 추가
ws.append(['제목','링크','날짜','본문'])

keyword=input('검색어를 입력하세여 >>')
page = int(input('몇 페이지까지 크롤링할꺼?'))     # 사용자로부터입력받은 숫자

for p in range(1,page+1):

    response = requests.get(f'https://kin.naver.com/search/list.naver?query={keyword}&page={p}')
    html = response.text
    soup=BeautifulSoup(html,'html.parser')

    # 1페이지 질문 10개 (태그객체)
    lis = soup.select('.basic1>li')
    i=1
    for li in lis:
        #링크태그
        anchor=li.select_one('._searchListTitleAnchor')  #dt >a 가능
        #제목
        title=anchor.text
        #링크
        link=anchor.attrs['href']
        #날짜
        date=li.select_one('.txt_inline').text
        #내용
        content=li.select_one('.txt_inline+dd').text #dd:nth-of-type(2) dd:nth-child(3) 가능

        print(i, title, link, date, content, sep= '\n')
        ws.append([title, link, date, content])
        i+=1

wb.save(f'04_requests 사용법{keyword}.xlsx')
'''

###6단계  -상세페이지 크롤링

keyword=input('검색어를 입력하세여 >>')
page = int(input('몇 페이지까지 크롤링할꺼?'))     # 사용자로부터입력받은 숫자

for p in range(1,page+1):

    response = requests.get(f'https://kin.naver.com/search/list.naver?query={keyword}&page={p}')
    html = response.text
    soup=BeautifulSoup(html,'html.parser')

    # 1페이지 질문 10개 (태그객체)
    lis = soup.select('.basic1>li')
    i=1
    for li in lis:
        #링크태그
        anchor=li.select_one('._searchListTitleAnchor')  #dt >a 가능
        #제목
        title=anchor.text
        #링크
        link=anchor.attrs['href']
        #날짜
        date=li.select_one('.txt_inline').text
        
        # 상세페이지요청
        response=requests.get(link)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        
        #예외처리 -문법상 오류없는데 오류가 날수도있음 - 에러가 나면 except로 넘어감
        try:
            contents=soup.select_one('.c-heading__content').text.strip()
        except:
            #본문이 없는경우
            contents=''

        print(i, title, link, date, contents, sep= '\n')
        i+=1

        ##셀렉트원 - 매칭되는 태그가 없으면 none 객체 반환
        ## 셀렉트 - 매칭되는 태그가 없으면 빈리스트반환 ([])
        #ontents=soup.select_one('.c-heading__content').text
        #AttributeError: 'NoneType' object has no attribute 'text'
        