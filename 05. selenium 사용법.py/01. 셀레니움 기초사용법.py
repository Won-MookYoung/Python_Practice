#오타주의
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('http://www.naver.com')
driver.maximize_window()   #최대화
driver.implicitly_wait(10)   #데이터를 찾는데 n초정도는 기다릴수있다

#element / elements 주의 한개일땐 element 다수일땐 s붙여서!!!!

#로그인 버튼 
# login_btn=driver.find_element(By.CSS_SELECTOR, '#account > a')  # <-로그인버튼 태그
# login_btn.click()         # 객체의 클릭 매서드가있는걸 실행해줌

#검색창
# search=driver.find_element(By.CSS_SELECTOR, '#query')
# # 크롬아 찾아줘 요소를 (CSS셀렉터 (선택자)에 의해서 , 선택자는 이거)

# search.send_keys('에어컨')   #검색창에 키워드입력
# search.send_keys(Keys.ENTER)  #엔터치기
login_btn=driver.find_element(By.CSS_SELECTOR, '#account > a')  # <-로그인버튼 태그
login_btn.click()

login=driver.find_element(By.CSS_SELECTOR, '#id')
login.send_keys('wmy1766')
login=driver.find_element(By.CSS_SELECTOR, '#pw')
login.send_keys('0123qwer!')

# login.send_keys(Keys.ENTER)
login=driver.find_element(By.CSS_SELECTOR, '#log\.login') 
login.click()

id = 'wmy1766'
pw = '0123qwer!'

pyperclip.copy(id)
driver.find_element_by_id('id').send_keys(Keys.CONTROL + 'v')
pyperclip.copy(pw)
driver.find_element_by_id('pw').send_keys(Keys.CONTROL + 'v')
time.sleep(0.7)
driver.find_element_by_id('log.login').click()
time.sleep(1)

login=driver.find_element(By.CSS_SELECTOR, '#log\.login') 
login.click()