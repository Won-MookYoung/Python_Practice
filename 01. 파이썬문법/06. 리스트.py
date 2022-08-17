'''
company_list=['애플','구글','테슬라']
company_list.append('아마존')

print(company_list)

person_info_list =[
    ['유재석',51,'남'],
    ['노홍철',44,'남'],
    ['하하',44,'남']
]
print(person_info_list[0][0])
'''

# 리스트
# 여러개의 데이터를 저장하는 자료형

# 변수 = [데이터,데이터,데이터]
company_list = ['삼성전자','카카오','네이버']

#데이터 접근하기
# print(company_list[2])
# print(company_list[-1])     # -1 : 맨 마지막 원소를 뜻함

company_list[0]='애플'
company_list[1]='구글'
company_list[2]='테슬라'

print(company_list)

#데이터 추가하기
company_list.append('아마존')    #append : 맨뒤에추가
print(company_list)

#리스트 길기
print(len(company_list))

#리스트 삭제
del company_list[0]     # 0번 삭제
print(company_list)