## 하나의 클래스로부터 여러개의 객체가 나올수있다
# 클래스 : 제품의설계도
# 객제: 설계도로만든 제품
# 속성 : 클래스안의변수
# 메서드 : 클래서안의 함수
# 생성자 : 객체를 만들때 처음 실행되는함수
# 인스턴스 : 메모리에 살아있는객체  = 객체
#class 클래스이름 :
    #def 메서드이름(self):      #self : 객체 자기자신
      #명령블록
#객체 = 클래스이름()
#객체.메서드()      #객체의 메서드


class Monster:                        #클래스
    def __init__(self,name,hp):       #생성자 #생성자에서 속성을 부여
        self.name=name         #객체 자기자신의 네임은    
        self.hp=hp         #속성추가
    def say(self): 
        print(f'나는 {self.name} 체력이{self.hp}이지')
    def hp_upgrade(self, plus):
        self.hp += plus
    def skill(self,skill_name):    #무조건 셀프가 처음에 들어가야함
        print(skill_name, '공격!')

shark =Monster('상어',300) # 객체명
shark.say()
#shark.name='엄마상어'     #속성변경가능
#print(shark.name)   #속성 =상어 

pikachu=Monster('피카츄',100)
pikachu.hp_upgrade(75)
pikachu.say()
pikachu.skill('아이언테일')    # 셀프 다음 스킬내임으로 들어가고 
