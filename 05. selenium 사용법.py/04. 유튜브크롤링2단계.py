# 스크롤을 n번 내리고 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url=('https://www.youtube.com/results?search_query=%EB%8F%88%EB%B2%84%EB%8A%94%EB%B2%95')

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
    title= info.find_element(By.CSS_SELECTOR, '.yt-simple-endpoint.style-scope.ytd-video-renderer')
    view = info.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(1)')   #가상선택자사용
    date = info.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(2)')
                                               #메타데이터라인의 스팬 두번째 자식                          

    print(f'{i}번째 영상',title.text, view.text, date.text, sep='\n')