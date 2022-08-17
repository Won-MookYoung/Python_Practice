'''
랜덤으로 1~100까지의 숫자를 고르면 
그게 업앤 다운인지 출력하고 
맞추면 몇번만에 맞췄는지 출력해


1. 랜덤숫자 지정
2. 입력숫자
3. 높으면 다운
4. 낮으면 업
5. 맞으면 출력
6. 카운트

'''


import random
rannum=random.randint(1,100)
count=1

while True:
    choose = int(input('(1~100) 숫자를 선택하세요 >>'))
    
    if choose >rannum:
        print('입력숫자 : {} , down입니다.'.format(choose))
    elif choose< rannum:
        print('입력숫자 : {} , up입니다.'.format(choose))
    else:
        print('정답입니다!!')
        print('{}번 만에 맞췄습니다.'.format(count))
        break

    count+=1
