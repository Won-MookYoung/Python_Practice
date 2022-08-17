# 순서가있는 
## 리스트
## range객체
## 문자열 

#for 문
## 리스트활용
'''
num_list=[1,2,3]
for num in num_list    1을먼저 저장하고 print()실행
                       그다음 2 저장하고 print()실행
                       그다음 3 저장하고 실행
                       리스트 있을때까지 실행 
print(num*2)'''

## rnage명령어 활용
'''
range(10) : 0~9까지 순서열을 반환
range(1,10) : 1~9까지 순서열을 반환
range(1,10,2) : 1~9까지 2단위로 1,3,5,7,9
for i in range(1,10) : 1~9까지 저장해서 실행
print(f'{i}번째 페이지) : 1~9번째 페이지 순서대로나옴'''

# 반복문
# 특정명령들을 반복해서 사용하고 싶을때 사용
#num_list = [1,2,3]
#for num in num_list:      #in 뒤부터 확인! 
                          #1,2,3 순서대로 하겠다 
    #print(num*2)
 #   print(num*2,end='')  #end : 마지막에 어떤걸로 마무리할것인지
                         #기본값 : end='\n'이 있는거
    #print(num*2,end=' ')

#for i in range(1,6):
#    print(f'{i}번째 페이지 크롤링중입니다.')
for i in range(10):
    print(f'{i}번째 페이지 크롤링중입니다.')