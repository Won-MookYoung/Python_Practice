'''
i=1    #반복을 돌릴 조건 세팅
while i<=10:     #i가 10보다 작거나 같을때까지 (트루일때까지반복)
    print(f'{i}번쨰)
    i=i+1   #11=10+1 일때 프로그램 종료       
'''
'''
무한반복
x=input('종료하려면 exit를 입력하세요')
if x=='exit':      
    break

'''
# while 문
# 조건이 False가 될때까지 반복
'''
i=1  # 초기식 세팅
while i <=10:   # 조건식
    print(f'{i}번째 자동화 작업입니다.')
    i = i+1     # 증감식
'''

while True:
    x = input('종료하려면 exit를 입력하세요>>')
    if x== 'exit':
        break  