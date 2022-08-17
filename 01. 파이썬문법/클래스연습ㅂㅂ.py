## 과자 클래스

class Snack:
    def __init__(self,name, price,taste):          #생성자 constructor
        self.name=name                             #속성 초기화 : 매개변수에들어온 속성이랑 매칭을 시켜줌
        self.price=price
        self.taste=taste


# 클래스로부터 객체를 만들수있다. 
Snack('콘칩',1500,'옥수수맛')     #콘칩 객체가 만들어짐 - 그냥두면 사라지니 변수에 담이줌
cornchip= Snack('콘칩',1500,'옥수수맛')
print(cornchip.name)
print(cornchip.price)

Snack('바나나킥',2000,'바나나맛')
bananakick=Snack('바나나킥',2000,'바나나맛')

class Snack:
    def __init__(self,name, price,taste):          #생성자 constructor
        self.name=name                             #속성 초기화 : 매개변수에들어온 속성이랑 매칭을 시켜줌
        self.price=price
        self.taste=taste
    # 매서드(method)
    def sale(self,percent):
        self.price = self.price * (100-percent)/100

Snack('바나나킥',2000,'바나나맛')
bananakick=Snack('바나나킥',2000,'바나나맛')

bananakick.sale(50)
print(bananakick.price)
