'''
지식인에 파이썬 크롤링

1단계 - 1페이지 첫번쨰 질문의 제목 날짜 설명 링크   hrif 속성?
2단계 - 1페이지 전체 질문의 제목 날짜 설명 링크
3단계 - n페이지 전체 질문의 제목 날짜 설명 링크 (사용자입력)
4단계 - 키워드 변경 (사용자입력)
5단계 - 엑셀추가
6단계 - 상세페이지 크롤링  # 질문 물어본거 클릭해서 하나하나
'''

#1단계
# import requests
# from bs4 import BeautifulSoup

# response=requests.get('https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%EC%A7%80%EC%8B%9D%EC%9D%B8&c_id=&c_name=&sm=tab_pge&kin_start=1&kin_age=0')
# html=response.text
# soup=BeautifulSoup(html,'html.parser')
 
# know_1title=soup.select_one('.api_txt_lines.question_text')
# print(know_1title.text)  #1.제목
# know_1day=soup.select_one('.desc')
# print(know_1day.text)    #1.날짜
# know_1exp=soup.select_one('.api_txt_lines.answer_text')
# print(know_1exp.text)    #1.설명
# know_1link=soup.select_one('.question_group>a')
# print(know_1link['href'])   #1.링크
 


#2단계
# import requests
# from bs4 import BeautifulSoup

# response=requests.get('https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%EC%A7%80%EC%8B%9D%EC%9D%B8&c_id=&c_name=&sm=tab_pge&kin_start=1&kin_age=0')
# html=response.text
# soup=BeautifulSoup(html,'html.parser')
# i=1
# know_1p_title=soup.select('.kin_wrap.api_ani_send')
# for page in know_1p_title:
#     title=page.select_one('.api_txt_lines.question_text')
#     day=page.select_one('.desc')
#     explain=page.select_one('.api_txt_lines.answer_text')
#     link=page.select_one('.question_group>a')
#     print(i,title.text, day.text, explain.text, link['href'], sep='\n')
#     i+=1



#3단계
# import requests
# from bs4 import BeautifulSoup

# page_number=input('몇 페이지까지 크롤링할까요 ?')
# what_page=0
# for n in range(1,int(page_number)+1):
#     what_page+=1
#     print('{}번 페이지'.format(what_page))
#     page_num=str((int(page_number)-1))
#     response=requests.get('https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%EC%A7%80%EC%8B%9D%EC%9D%B8&c_id=&c_name=&sm=tab_pge&kin_start='+str(n-1)+'1&kin_age=0')
#     html=response.text
#     soup=BeautifulSoup(html,'html.parser')

#     i=1
#     know_1p_title=soup.select('.kin_wrap.api_ani_send')
#     for page in know_1p_title:
#         title=page.select_one('.api_txt_lines.question_text')
#         day=page.select_one('.desc')
#         explain=page.select_one('.api_txt_lines.answer_text')
#         link=page.select_one('.question_group>a')
#         print(i,title.text, day.text, explain.text, link['href'], sep='\n')
#         i+=1


#4단계
# import requests
# from bs4 import BeautifulSoup

# page_number=input('몇 페이지까지 크롤링할까요 ?')
# keword=input('무엇을 검색할까요 ?')
# what_page=0
# for n in range(1,int(page_number)+1):
#     what_page+=1
#     print('{}번 페이지'.format(what_page))
#     page_num=str((int(page_number)-1))
#     response=requests.get('https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query='+keword+'&c_id=&c_name=&sm=tab_pge&kin_start='+str(n-1)+'1&kin_age=0')
#     html=response.text
#     soup=BeautifulSoup(html,'html.parser')

#     i=1
#     know_1p_title=soup.select('.kin_wrap.api_ani_send')
#     for page in know_1p_title:
#         title=page.select_one('.api_txt_lines.question_text')
#         day=page.select_one('.desc')
#         explain=page.select_one('.api_txt_lines.answer_text')
#         link=page.select_one('.question_group>a')
#         print(i,title.text, day.text, explain.text, link['href'], sep='\n')
#         i+=1



#5단계
# import requests
# from bs4 import BeautifulSoup
# import openpyxl

# wb=openpyxl.Workbook()
# ws = wb.create_sheet('지식인 크롤링')
# ws['A1']= '제목'     
# ws['B1']= '작성날짜'
# ws['C1']= '본문'
# ws['D1']= 'URL'
# ws['A2']= ' '
# ws['B2']= ' '
# ws['C2']= ' '
# ws['D2']= ' '

# page_number=input('몇 페이지까지 크롤링할까요 ?')
# keword=input('무엇을 검색할까요 ?')
# what_page=0
# for n in range(1,int(page_number)+1):
#     what_page+=1
#     print('{}번 페이지'.format(what_page))
#     page_num=str((int(page_number)-1))
#     response=requests.get('https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query='+keword+'&c_id=&c_name=&sm=tab_pge&kin_start='+str(n-1)+'1&kin_age=0')
#     html=response.text
#     soup=BeautifulSoup(html,'html.parser')

#     i=1
#     know_1p_title=soup.select('.kin_wrap.api_ani_send')
#     for page in know_1p_title:
#         title=page.select_one('.api_txt_lines.question_text')
#         day=page.select_one('.desc')
#         explain=page.select_one('.api_txt_lines.answer_text')
#         link=page.select_one('.question_group>a')
#         print(i,title.text, day.text, explain.text, link['href'], sep='\n')
#         i+=1

#         ws.append([title.text, day.text, explain.text, link['href']])

#     wb.save('지식인 크롤링.xlsx')




# # 6단계
import requests
from bs4 import BeautifulSoup

page_number=input('몇 페이지까지 크롤링할까요 ?')
keword=input('무엇을 검색할까요 ?')
what_page=0
for n in range(1,int(page_number)+1):
    what_page+=1
    print('{}번 페이지'.format(what_page))
    page_num=str((int(page_number)-1))
    response=requests.get('https://search.naver.com/search.naver?where=kin&kin_display=10&qt=&title=0&&answer=0&grade=0&choice=0&sec=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query='+keword+'&c_id=&c_name=&sm=tab_pge&kin_start='+str(n-1)+'1&kin_age=0')
    html=response.text
    soup=BeautifulSoup(html,'html.parser')

    i=1
    know_1p_title=soup.select('.kin_wrap.api_ani_send')
    for page in know_1p_title:
        title=page.select_one('.api_txt_lines.question_text')
        day=page.select_one('.desc')
        explain=page.select_one('.api_txt_lines.answer_text')
        link=page.select_one('.question_group>a')
        print(i,title.text, day.text, explain.text, link['href'], sep='\n')
        i+=1

        url= link['href']
        response2=requests.get(url)
        html2=response2.text
        soup2=BeautifulSoup(html2,'html.parser')
        x=1
        details=soup2.select('.se-module.se-module-text')
        for detail in details:
            print(f'답변 {x}',detail.text, sep='\n')
            x+=1

