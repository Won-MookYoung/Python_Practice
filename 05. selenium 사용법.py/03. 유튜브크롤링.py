from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url=('https://www.youtube.com/results?search_query=%EB%8F%88%EB%B2%84%EB%8A%94%EB%B2%95')

driver = webdriver.Chrome('c:/chromedriver.exe')
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

# 처음 접속했을때 영상의 제목 조회수 날짜 크롤링
# 영상 1개의 정보 가지는 태그 30개 추출 -> 리스트
infos=driver.find_elements(By.CSS_SELECTOR, 'div.text-wrapper')

# i=1
# for info in infos:
#     #제목 조회수 날짜 크롤링
#     title= info.find_element(By.CSS_SELECTOR, '.yt-simple-endpoint.style-scope.ytd-video-renderer')
#     view = info.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(1)')   #가상선택자사용
#     date = info.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(2)')
#                                                #메타데이터라인의 스팬 두번째 자식                          

#     print(f'{i}번째 영상',title.text, view.text, date.text, sep='\n')
#     i+=1

# i=1 따로 안하고싶을때
for i, info in enumerate(infos, 1):   
    #제목 조회수 날짜 크롤링
    title= info.find_element(By.CSS_SELECTOR, '.yt-simple-endpoint.style-scope.ytd-video-renderer')
    view = info.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(1)')   #가상선택자사용
    date = info.find_element(By.CSS_SELECTOR, '#metadata-line > span:nth-child(2)')
                                               #메타데이터라인의 스팬 두번째 자식                          

    print(f'{i}번째 영상',title.text, view.text, date.text, sep='\n')