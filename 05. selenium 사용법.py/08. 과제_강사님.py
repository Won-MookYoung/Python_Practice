# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import openpyxl

# url = 'https://search.shopping.naver.com/search/all?query=%EC%97%AC%EB%A6%84&cat_id=&frm=NVSHATC'

# webdriver.Chrome('c:/chromedriver.exe')

# driver = webdriver.Chrome('c:/chromedriver.exe')
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(5)

# # 1단계 스크롤하기전 상품 크롤링
# item_list=driver.find_elements(By.CSS_SELECTOR, '.basicList_item__2XT81')

# for i, item in enumerate (item_list,1):
#     #링크태그
#     link_tag = item.find_element(By.CSS_SELECTOR,'.basicList_link__1MaTN')
#     #상품명
#     product = link_tag.text    #(링크태그의 텍스트는 상품명일거고)
#     #상세페이지 링크
#     link= link_tag.get_attribute('href')
#     #가격
#     price = item.find_element(By.CSS_SELECTOR,'.price_num__2WUXn').text          #찾은거의 텍스트만 추출하겠다
#     #이미지 주소
#     img_src = item.find_element(By.CSS_SELECTOR,'.thumbnail_thumb__3Agq6 >img').get_attribute('src')  
#                                                 # 이미지 위의 클래스이름

#     print(product, link, price, img_src, sep='\n')





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import openpyxl
import urllib.request

wb=openpyxl.Workbook()
ws=wb.active
ws.append(['상품명','상세페이지 링크',' 가격',' 이미지주소'])

keyword=input('키워드')
page = int(input('페이지'))

driver = webdriver.Chrome('c:/chromedriver.exe')
driver.implicitly_wait(5)
for i in range(1,page+1):
    url = f'https://search.shopping.naver.com/search/all?query={keyword}&pagingIndex={i}&paginSize=40'
    driver.get(url)
    actions = ActionChains(driver)
    
    #스크롤 전 아이템 개수확인
    
    item_list=driver.find_elements(By.CSS_SELECTOR, '.basicList_item__2XT81')
    
    before_count=len(item_list)

    while True:
        #맨아래로 스크롤을 내려줌
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
        #스크롤사이 로딩시간
        time.sleep(1)
        #스크롤 후 아이템 개수
        item_list=driver.find_elements(By.CSS_SELECTOR, '.basicList_item__2XT81')
        len(item_list)
        after_count=len(item_list)

        #스크롤 전 후 비교
        if before_count == after_count:
            break
        #아이템 갯수 업데이트
        before_count = after_count

    for i, item in enumerate (item_list,1):
        actions.move_to_element(item).perform()
        #링크태그
        link_tag = item.find_element(By.CSS_SELECTOR,'.basicList_link__1MaTN')
        #상품명
        product = link_tag.text    #(링크태그의 텍스트는 상품명일거고)
        #상세페이지 링크
        link= link_tag.get_attribute('href')
        #가격
        price = item.find_element(By.CSS_SELECTOR,'.price_num__2WUXn').text          #찾은거의 텍스트만 추출하겠다
        #이미지 주소
        img_src = item.find_element(By.CSS_SELECTOR,'.thumbnail_thumb__3Agq6 >img').get_attribute('src')  
                                                    # 이미지 위의 클래스이름

        print(product, link, price, img_src, sep='\n')
        ws.append([product, link, price, img_src])

        #이미지 저장
        urllib.request.urlretrieve(img_src,f'05. selenium 사용법/img/{product}.jpg')

wb.save(f'05.selenium 사용법/{keyword}_쇼핑.xlsx')