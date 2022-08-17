import requests
from bs4 import BeautifulSoup


# 리스폰스 객체의 텍스트속성에는 html이 들어있다
response = requests.get('http://www.naver.com')#겟요청을 주다
html = response.text     #객체의 텍스트속성에 들어있는 html을 텍스트로 읽기
soup = BeautifulSoup(html, 'html.parser') #뷰티풀스프는 클래스
                            #from import : import뒤의 클래스만 사용하고싶을때 사용
                        #클래스로 객체를 만듬 
                     #(첫번째로 객체 html 을 넣어주고 두번쨰로 분석할 parser를 넣어줌)

home_btn=soup.select_one('#NM_set_home_btn')   #soup객체가 이 태그를 찾아줌
print(home_btn.text)  
# 서버에 요청 -> html로 받음 -> 거기서 찾아줌

'''soup 은 html 을 하나하나 쪼개서 객체로 가지고있다.
<div></div> ... <p></p> 이런식으로
그래서 soup.select_one('asdasd') 하면 그 쪼개진 html에서 asdasd라는 객체를 찾는것!'''