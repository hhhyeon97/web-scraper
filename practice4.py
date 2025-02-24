
# OOP
# 객체 지향 프로그래밍 

# [22. OOP - Class, Method, Inheritance]

"""
OOP란 데이터와 기능을 하나의 객체로 묶어, 
코드의 재사용성과 유지보수성을 높이는 프로그래밍 패러다임이다.

현실 세계의 개념을 코드로 표현하여 
확장성, 보안성, 유연성을 높이는 프로그래밍 방식이다.
"""

# 예시)
# 🔎 기존 방식 (절차 지향)
Lee = {
    "name":"Lee",
    "XP":1000,
    "team":"T1"
}

def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")

introduce_player(Lee) # Hello! My name is Lee and I play for T1

# 🔎 OOP 방식 (클래스 사용)
class Player:
    def __init__(self, name, xp, team):
        self.name = name
        self.xp = xp
        self.team = team
    
    def introduce(self):
        print(f"Hello! My name is {self.name} and I play for {self.team}")

# 객체 생성
player1 = Player("Lee", 1000, "T1")
player1.introduce() # Hello! My name is Lee and I play for T1

"""
기존 방식과 차이점

1. 데이터와 기능의 결합

기존 방식은 데이터(딕셔너리)와 기능(함수)이 분리되어 있음.
OOP 방식은 데이터(속성)와 기능(메서드)이 한 곳(클래스)에서 관리됨.

2. 확장성과 유지보수

기존 방식은 새 플레이어를 추가하려면 딕셔너리를 만들고 별도로 함수를 호출해야 함.
OOP 방식은 Player 객체를 만들기만 하면 자동으로 기능이 포함됨.
"""

#=========================
# Class

"""class Puppy:
    pass

poodle = Puppy() 
print(poodle) # <__main__.Puppy object at 0x000001B637EFAAB0>
# poodle이 Puppy 객체인 것을 알 수 있다."""


#=========================
# Method
# class 안에 있는 함수이다.

"""
Method vs Function

함수(Function): 클래스와 관계없이 독립적으로 정의된 코드 블록
메서드(Method): 클래스 내부에 정의된 함수로, 특정 객체에서 동작

클래스 밖에서 정의되면 함수(Function), 클래스 안에서 정의되면 메서드(Method)이다.
"""


# 잘못된 메서드 예시

"""class Puppy:
    def __init__():
        print("Puppy is born!")

poodle = Puppy() 
print(poodle) # TypeError: Puppy.__init__() takes 0 positional arguments but 1 was given
"""

"""
위 에러에서 알 수 있는 것

Puppy 객체를 생성하면 파이썬은 자동으로 __init__() 메서드를 호출한다.
__init__() 메서드가 0개의 인자를 받도록 정의되었지만, 1개의 인자가 전달되었다는 오류 발생
현재 __init__() 메서드는 인자를 정의하지 않음.
하지만 파이썬은 메서드를 호출할 때 자동으로 인스턴스를 첫 번째 인자로 전달한다!
즉, 첫 번째 인자로 self를 받아야 객체 자신을 참조할 수 있음

결론 !
클래스의 메서드는 자동으로 인스턴스를 첫 번째 인자로 받기 때문에
이를 나타내기 위해 self를 사용해야 한다.
"""

# 올바른 코드 (self 추가)
"""class Puppy:
    def __init__(self):  # 첫번째 인자로 self가 자동 전달됨
        print(self) # <__main__.Puppy object at 0x000002017EB4AD20>
        print("Puppy is born!")

poodle = Puppy()  # 정상적으로 실행됨 Puppy is born!
print(poodle) # <__main__.Puppy object at 0x000002017EB4AD20>

# __init__() -> 클래스의 기본 값을 세팅하는 역할을 하는 곳
# 객체가 만들어질 때 실행되는 생성자 메서드이다.
# 객체가 생성될 때 자동으로 실행되며 인스턴스의 초기 상태(속성 값)를 설정하는 역할을 한다.
# 인스턴스의 속성을 설정하거나 필요한 초기 작업을 수행할 수 있음"""


""" 위 같은 출력을 볼 때 메모리 주소가 같다는 것을 알 수 있다.

★ 클래스의 모든 메서드는 첫 번째 인자로 자기 자신(self)을 참조한다.

설명 추가
poodle = Puppy()를 실행하면, 객체가 생성될 때 __init__() 메서드가 호출됨
print(self)를 통해 self가 poodle과 같은 객체를 참조하고 있음을 확인할 수 있음
즉, 클래스 내부에서 정의된 모든 인스턴스 메서드는 
첫 번째 인자로 자기 자신(self)을 자동으로 받음

결론 !
클래스의 모든 인스턴스 메서드는 
첫 번째 인자로 객체 자신(self)을 참조하여
해당 객체의 속성과 메서드에 접근할 수 있도록 한다.
"""

"""
🔎 인스턴스(instance) 
클래스로부터 생성된 객체이다.
💡 ex ) poodle = Puppy()에서 poodle이 Puppy 클래스의 인스턴스이다.

🔎 인스턴스 메서드(instance method)
인스턴스가 호출할 수 있는 메서드로, 첫 번째 인자로 항상 self(해당 인스턴스)를 받는다.

🔎 한 줄 정리
인스턴스는 클래스에서 만들어진 객체이며
인스턴스 메서드는 해당 객체가 사용할 수 있는 함수이다.
"""
# ========================================================
"""class Puppy:
    def __init__(self):
        self.name = "키키"
        self.age = 0.1
        self.breed = "Beagle" 

kiki = Puppy()
print(kiki.name, kiki.age, kiki.breed) # 키키 0.1 Beagle
mimi = Puppy()
print(mimi.name, mimi.age, mimi.breed) # 키키 0.1 Beagle"""

# mimi가 kiki와 같은 정보를 출력한다는 걸 알 수 있다.
# 각각의 강아지가 다른 값을 출력할 수 있게 커스텀하려면 !

class Puppy:
    def __init__(self, name, breed):  # 초기값 설정
        self.name = name  
        self.age = 2 # 하드코딩한 값 
        self.breed = breed

kiki = Puppy("키키", "Poodle")  # 객체 생성 시 초기 값 설정
mimi = Puppy("미미", "Beagle")

print(kiki.breed, mimi.breed) # Poodle Beagle

# 💡 좀 더 가독성 있게 argument명을 매칭해서 써도 됨!!
kiki = Puppy(name="키키", breed="Poodle")
mimi = Puppy(name="미미", breed="Beagle")

# =====================================================

# 다양한 메서드가 있음
# ex) __str__()
# 클래스 전체를 print하려고 할 때 자동으로 호출한다.
# ㄴ 객체 자체를 출력할 때 넘겨주는 형식을 지정해주는 메서드이다.

class Hi:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"hi ~ {self.name}"

test = Hi("Lee")
print(test) # hi ~ Lee