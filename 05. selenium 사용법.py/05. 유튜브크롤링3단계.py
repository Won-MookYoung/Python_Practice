# 스크롤을 n번 내리고 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl

def text_to_num(text):
    #숫자로 변경
    text=text.replace('조회수', '').replace('회','').strip()
    if '억' in text:
        num=float(text.replace('억',''))*100000000
    elif '만' in text:
        num=float(text.replace('만',''))*10000
    elif '천' in text:
        num=float(text.replace('천',''))*1000
    elif '없음'== text:
        num=0
    else:
        num=int(text)

    return num


wb = openpyxl.Workbook()
ws= wb.active

ws.append(['제목','조회수','날짜'])


# 검색어변경, 엑셀저장
search = input('검색어를 입력하세요 :')

url=('https://www.youtube.com/results?search_query='+search)

driver = webdriver.Chrome('c:/chromedriver.exe')
driver.get(url)                           #url 접속
driver.maximize_window()                  #화면크게
driver.implicitly_wait(5)                 #5초정도 기다림 엘리먼트 찾는거 

#스크롤을 n번 내리고 크롤링
for i in range(1,5):                      #4번정도 스크롤내림 
    driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)   # END 키를 누르겠다 
    #스크롤 사이 로딩시간                                               # END : 스크롤을 맨 밑으로 내리는거
    time.sleep(2)                                                     

infos=driver.find_elements(By.CSS_SELECTOR, 'div.text-wrapper')

for i, info in enumerate(infos, 1):   
    #제목 조회수 날짜 크롤링
    try:
        title= info.find_element(By.CSS_SELECTOR, '.yt-simple-endpoint.style-scope.ytd-video-renderer').text
        view = info.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(1)').text   #가상선택자사용
        date = info.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(2)').text
    
    except:
        continue                                          #메타데이터라인의 스팬 두번째 자식                          
    
    view = text_to_num(view)   #조회수 350만회
    print(f'{i}번째 영상',title, view, date, sep='\n')
    ws.append([title, view, date])

wb.save(f'유튜브 {search} 검색 크롤링.xlsx')