#구구단 만드는 프로그램
#데이터입력 : 몇단을 출력할까요?
#데이터 출력 : 7* 1 = 7 ~ 7*9=73

#rnrneks = int(input('몇 단을 출력할까요?>>>'))
#for i in range(2,10):
#    for j in range(1,10):
#        print('{}+{}={}'.format(i,j,i*j))



'''
x=int(input('몇단?'))
for i in range(1,10):
    #print('{}*{}={}'.format(rnrneks,i,rnrneks*i))
    print(f'{x}*{i}={x*i}')


x=int(input('ㅁㅁㄴㅇㅁㄴㅇ'))
for i in range(1,10):
    print(f'{x}*{i}={x*i}')
'''
#구구단 몇단까지 출력할까요
x= int(input('몇단까지?'))
for j in range(2,x+1):
    print(f'==={j}단===')
    for i in range(1,10):
        print(f'{j}*{i}={j*i}')