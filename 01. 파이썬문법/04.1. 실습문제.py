# 사용자로부터 크롤링할 페이지 개수를 입력받으면, 
# 메시지 출력하기

#데이터입력
#크롤링할 페이지 개수를 입력하세요 >>>10
#데이터출력
#크롤링할 페이지 개수는 10개 입니다.
x=input('크롤링할 페이지 개수를 입력하세요 >>>')
print('크롤링할 페이지 개수는',x+'개 입니다.')
print('크롤링할 페이지 개수는 {}개 입니다.'.format(x))


#그냥 변수를 만들어도 되지만 데이터를 나타내는 변수로 나타내는게 좋음
#page_number= int(input('크롤링할 페이지 개수를 입력하세요>>>'))
#print(page_number)
#print('크롤링할 페이지 개수는' +page_number+'개입니다.)
#라고 하면 오류가 남 
#file 'c:\~~~~.실습문제.py' line n,~~
#typeError : can only concatenate str (not'int') to str
#str이랑 str만 결합할수있다 int는 안된다
#print('크롤링할 페이지 개수는' +str(page_number)+'개입니다.)
#로 변환해주면됨 

#문자열 포매팅 f스트링
message=f'크롤링할 페이지 개수는 {x}개입니다.'
print(message)
