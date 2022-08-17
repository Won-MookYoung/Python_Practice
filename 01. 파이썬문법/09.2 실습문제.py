# 업엔다운게임을 만들어보자
# 프로그램이 시작되면 컴퓨터가 
# 1부터 100까지중 랜덤으로 하나의 번호를 고른다
# 사용자는 해당 번호를 맞출때까지 입력
#번호를 맞추면 총시도 횟수를 출력한다

#실행결과 
#컴퓨터가 숫자를 골랐습니다.
#(1~100) 숫자를 맞춰보세요 >>> 50 up입닌다.
#(1~100) 숫자를 맞춰보세요 >>> 75 down입니다 ...
# ...
# 총시도 횟수 7 

    
'''
import random
luck=random.randint(1,100)
cnt=1
while True:
    num=int(input('숫자를 입력해주세요: '))
    
    if num > luck:
        print('(1~100) 숫자를 맞춰보세요 >> {} down입니다.'.format(num))
        
    elif num < luck:
        print('(1~100) 숫자를 맞춰보세요 >> {} up입니다.'.format(num))
            
    else:
        print('총 시도 횟수 :{}'.format(cnt))  
        break
    
    cnt+=1
   ''' 

import random

number=random.randint(1,100)
print('컴퓨터가 숫자를 골랐음')
# 반복횟수
try_count=1
while True:
    x = int(input ('(1~100)사이 숫자를 입력하세요'))

    if x == number:
        print('정답입니다.')
        print('총 시도횟수는', try_count)
        break
    elif x> number:
        print('down 입니다.')
    else:
        print('up 입니다.')
    
    #if문 다 끝나고 와일문으로 돌아가기전에 시도횟수 한번증가
    try_count +=1

