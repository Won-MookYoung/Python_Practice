# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome('C:/chromedriver.exe')
# user_id = 'wmy1766'
# user_pw = '0123qwer!'

# #1. 로그인페이지 이동
# driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
# driver.maximize_window()
# driver.implicitly_wait(5)

# #2. 아이디 입력
# id=driver.find_element(By.CSS_SELECTOR, '#id')
# id.send_keys(user_id)
# time.sleep(1.5)

# #3. 비밀번호 입력
# pw = driver.find_element(By.CSS_SELECTOR, '#pw')
# pw.send_keys(user_pw)
# time.sleep(1.5)

# #4. 로그인버튼 클릭
# login_btn = driver.find_element(By.CSS_SELECTOR,'#log\.login')
# login_btn.click()



#send_key 사용안하고 pyperclip으로 사용하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import pyautogui

driver = webdriver.Chrome('C:/chromedriver.exe')
user_id = 'wmy1766@naver.com'
user_pw = 'christmas1109'

#1. 로그인페이지 이동
driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net')
driver.maximize_window()
driver.implicitly_wait(5)

#2. 아이디 입력
id=driver.find_element(By.CSS_SELECTOR, '#id_email_2_label > span:nth-child(1)')
id.click()
pyperclip.copy(user_id)
pyautogui.hotkey('ctrl','v')
time.sleep(1.5)

#3. 비밀번호 입력
pw = driver.find_element(By.CSS_SELECTOR, '#id_password_3_label')
pw.click()
pyperclip.copy(user_pw)
pyautogui.hotkey('ctrl','v')
time.sleep(1.5)

#4. 로그인버튼 클릭
login_btn = driver.find_element(By.CSS_SELECTOR,'#login-form > fieldset > div.wrap_btn > button.btn_g.btn_confirm.submit')
login_btn.click()