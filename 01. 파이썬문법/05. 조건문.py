name='스타트코딩'
age=19


if age <20:                 
    print('미성년자입니다.') # if문의 명력블록
else:                       
    print('성인입니다.')     # else문의 명령블록

# 조건문 개념
# 조건에 따라 실행할 명령 선택

origin_pass = '1234'
input_pass = input('패스워드를 입력하세요 : ')

if input_pass == origin_pass:
    #조건A가 참일때 실행
    print('로그인 성공!')
    print('반갑습니다.')
elif input_pass == '':
    #조건A는 거짓, 조건B가 참일때 실행
    print('아무것도 입력하지 않았습니다')
else:
    #조건A,B 모두 거짓일때 실행
    print('로그인 실패')
    print('다시 시도해 주세요')
    