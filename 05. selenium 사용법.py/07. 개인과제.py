# 네이버 > 쇼핑 > '여름' 검색
# 상품명 가격 상세페이지링크 썸네일이미지주소 크롤링
# 키워드 변경
# 페이지 도 변경
# 엑셀저장

#1. 스크롤 전 크롤링
#2. 스크롤 끝까지 내리고 크롤링
#3. 페이지처리
#4. 검색어변경
#5. 엑셀저장
#6. 이미지저장(썸네일 img 폴더만들고 저장)
#7. 스크롤 얼마나 내릴지 모를때 알고리즘 어떻게 구성해야할지

### 1단계
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# url=('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%97%AC%EB%A6%84&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%97%AC%EB%A6%84&sort=rel&timestamp=&viewType=list')

# driver = webdriver.Chrome('c:/chromedriver.exe')
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(5)

# infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

# i=1
# for info in infos:
    
#     product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
#     price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
#     link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

#     print(f'{i}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
#     i+=1


### 2단계
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# url=('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%97%AC%EB%A6%84&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%97%AC%EB%A6%84&sort=rel&timestamp=&viewType=list')

# driver = webdriver.Chrome('c:/chromedriver.exe')
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(5)


# for x in range(1,6):                      
#     driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
#     time.sleep(2) 

# infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

# i=1
# for info in infos:
    
#     product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
#     price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
#     link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

#     print(f'{i}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
#     i+=1


### 3단계
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# page_num=input('페이지')
# driver = webdriver.Chrome('c:/chromedriver.exe')
# driver.get('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%97%AC%EB%A6%84&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%97%AC%EB%A6%84&sort=rel&timestamp=&viewType=list')
# driver.maximize_window()
# driver.implicitly_wait(5)

# for i in range(1,int(page_num)+1):
#     if i >=2:
#         url=('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%97%AC%EB%A6%84&pagingIndex={}&pagingSize=40&productSet=total&query=%EC%97%AC%EB%A6%84&sort=rel&timestamp=&viewType=list'.format(i))
#         driver.get(url)
#         driver.implicitly_wait(5)


#         for x in range(1,6):                      
#             driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
#             time.sleep(2) 

#         infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

#         a=1
#         for info in infos:
            
#             product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
#             price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
#             link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

#             print(f'{a}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
#             a+=1
#     else:
#         for x in range(1,6):                      
#             driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
#             time.sleep(2) 

#         infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

#         a=1
#         for info in infos:
            
#             product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
#             price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
#             link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

#             print(f'{a}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
#             a+=1


### 4단계
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# page_num=input('페이지')
# keyword=input('검색어')
# driver = webdriver.Chrome('c:/chromedriver.exe')
# driver.get('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={}&pagingIndex=1&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list'.format(keyword,keyword))
# driver.maximize_window()
# driver.implicitly_wait(5)

# for i in range(1,int(page_num)+1):
#     if i >=2:
#         url=('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={}&pagingIndex={}&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list'.format(keyword,i,keyword))
#         driver.get(url)
#         driver.implicitly_wait(5)


#         for x in range(1,6):                      
#             driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
#             time.sleep(2) 

#         infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

#         a=1
#         for info in infos:
            
#             product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
#             price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
#             link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

#             print(f'{a}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
#             a+=1
#     else:
#         for x in range(1,6):                      
#             driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
#             time.sleep(2) 

#         infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

#         a=1
#         for info in infos:
            
#             product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
#             price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
#             link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

#             print(f'{a}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
#             a+=1


###5단계
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import openpyxl

# wb = openpyxl.Workbook()
# ws = wb.active
# ws.append(['상품명','링크','가격'])

# keyword=input('검색어')
# page_num=input('페이지')

# driver = webdriver.Chrome('c:/chromedriver.exe')
# driver.get('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={}&pagingIndex=1&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list'.format(keyword,keyword))
# driver.maximize_window()
# driver.implicitly_wait(5)

# for i in range(1,int(page_num)+1):
#     if i >=2:
#         url=('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={}&pagingIndex={}&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list'.format(keyword,i,keyword))
#         driver.get(url)
#         driver.implicitly_wait(5)


#         for x in range(1,6):                      
#             driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
#             time.sleep(2) 

#         infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

#         a=1
#         for info in infos:
            
#             product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
#             price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
#             link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

#             print(f'{a}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
#             a+=1

#             ws.append([product.text, link.get_attribute('href'), price.text])
            
#     else:
#         for x in range(1,6):                      
#             driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
#             time.sleep(2) 

#         infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

#         a=1
#         for info in infos:
            
#             product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
#             price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
#             link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

#             print(f'{a}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
#             a+=1

#             ws.append([product.text, link.get_attribute('href'), price.text])

# wb.save(f'셀레니움 사용법 키워드-{keyword} .xlsx')


### 6단계
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl


wb = openpyxl.Workbook()
ws = wb.active
ws.append(['상품명','링크','가격'])

keyword=input('검색어')
page_num=input('페이지')

driver = webdriver.Chrome('c:/chromedriver.exe')
driver.get('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={}&pagingIndex=1&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list'.format(keyword,keyword))
driver.maximize_window()
driver.implicitly_wait(5)

for i in range(1,int(page_num)+1):
    if i >=2:
        url=('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={}&pagingIndex={}&pagingSize=40&productSet=total&query={}&sort=rel&timestamp=&viewType=list'.format(keyword,i,keyword))
        driver.get(url)
        driver.implicitly_wait(5)


        for x in range(1,6):                      
            driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
            time.sleep(2) 

        infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

        a=1
        for info in infos:
            
            product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
            price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
            link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

            print(f'{a}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
            a+=1

            ws.append([product.text, link.get_attribute('href'), price.text])
            

            
    else:
        for x in range(1,6):                      
            driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)                                                   
            time.sleep(2) 

        infos=driver.find_elements(By.CSS_SELECTOR, 'div.basicList_info_area__17Xyo')

        a=1
        for info in infos:
            
            product= info.find_element(By.CSS_SELECTOR, '.basicList_link__1MaTN')
            price = info.find_element(By.CSS_SELECTOR, '.price_num__2WUXn')   
            link = info.find_element(By.CSS_SELECTOR, 'a.basicList_link__1MaTN')                                                               

            print(f'{a}번째 상품',product.text, price.text, link.get_attribute('href'),sep='\n')
            a+=1

            ws.append([product.text, link.get_attribute('href'), price.text])
            
    
wb.save(f'셀레니움 사용법 키워드-{keyword} .xlsx')