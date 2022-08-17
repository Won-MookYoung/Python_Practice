#1. 매개변수와 결과값이 있는 함수
def sum(a,b):
    result=a+b
    return result    #리턴은 그 값을 반환해주는거 
                     # sum(a,b)만 넣으면 그 자체를 보여줌

#print(sum(5,2))

#2. 결과값이 없는 함수
# def print_sum(a,b):
    # print(a+b)    

# print_sum(1,2)


#3. 매개변수가 없는 함수
import random
def get_random_number():
    number = random.randint(1,10)
    return number

get_random_number()     #리턴했으니 get~() 이게 그 자리가됨
                        #프린트 해줘야함
print(get_random_number())          

#4. 매개변수도 없고, 결과값도 없는 함수
def print_hello():
    print('hello')

print_hello()