 # 함수를 사용하지 않은 경우
#  '''
# print('안녕하세요 ㅇㅇ')
# print('현재 프리미엄 서비스 사용기간이 30일 남았습니다.')

# print('안녕하세요 ㅁㅁ')
# print('현재 프리미엄 서비스 사용기간이 15일 남았습니다.')

# print('안녕하세요 ㅅㅅ')
# print('현재 프리미엄 서비스 사용기간이 10일 남았습니다.')
# '''
# 함수를 사용한 경우

def print_message(a,b):
    print(f'안녕하세요.{a}님')
    print(f'현재 프리미엄서비스기간이 {b}일 남았습니다.')

# print_message('동준',30)
# print_message('aa',33)
# print_message('bb',44)
# print_message('cc',11)
# print_message('dd',22)


#리스트랑 for문 함수 결합
info_list =[
    ['동준',30],
    ['원준',15],
    ['현식',22]
]
for info in info_list:
    print_message(info[0],info[1])     #인포0은 이름 인포1은 나이

