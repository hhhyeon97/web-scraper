
# Variables and Functions

# [0. 기본 출력]

print("Hello world!")

# [1. 변수] | variable
# 파이썬 코드는 위에서 아래로 동작한다.
# 형식 : 변수명 = 값

a = 2
b = 3
c = a+b
a = 1
b = 10
print(c) # 5

# ex )
# name = "Kim"
# age = 7
# print("Hello my name is",name)
# print("and I'm",age,"years old")

# <변수 규칙>
# 변수 명에 공백 x 숫자/특문으로 시작 x
# 파이썬에선 주로 snake case 사용 (선택사항)

# snake case
my_age = 88
# camel case
myAge = 88

# [2. 데이터 타입] | data type

# 숫자 number
address_number = 12345

# 문자열 string
my_name = "Lee"
print(my_name)

# 따옴표로 감싸면 어떤 값이든 문자열이 된다.
my_name = "12" 

# boolean
# 참(1)/거짓(0)
# 첫 글자는 대문자로 입력

my_type = True
my_type = False

# [3. 함수] | function
# 재사용 가능한 코드 덩어리

# 함수 정의
# 코드 들여쓰기(스페이스 2번 or 탭 키)
def say_hello():
    print("hello ~")

def say_bye():
    print("bye bye")

# 함수 실행
# say_hello()
# say_bye()

# 함수 안에 다른 함수를 넣을 수도 있다.
def test1():
    say_hello()

test1()

# [4. 매개변수] | parameter
# 함수 안으로 데이터를 보내 함수의 결과를 바꿀 수 있게 함

# user_name은 parameter라고 한다.
def say(user_name):
    print("hello",user_name,"!")

# print(name) <- 매개변수는 함수 내에서만 유효함

# Kim, Lee, Park은 argument(인수)라고 한다.
say("kim")
say("Lee")
say("Park")

# Parameter는 매개변수로서 함수를 정의할 때 필요한 변수 이름
# Argument는 전달 값으로서 함수를 콜할 때 실제로 넘어가는 값(데이터)

# [5. 다중 매개변수] | Multiple Parameters
# 파라미터는 함수로 전달하는 데이터를 저장하기 위한 
# placeholder(임시로 채워 놓는 내용물) 역할을 한다.

def say(user_name, user_age):
    print("hello",user_name,"!")
    print("you are",user_age,"years old.")

say("kim",12)

def bankbook(money):
    print(1000000000 + money)

bankbook(2000000)

# [6. 기본 매개변수] | Default Parameters

# 아래와 같이 실행했을 때 전달하는 실제 값이 없어서 오류 남
# 사용자가 user_name의 값을 주지 않았을 때
# 에러를 보여주는 것 보다 익명 값으로 방지하기

# def t1(user_name):
#     print("hello",user_name)

# t1()

# 해결
# 매개변수 기본 값 설정
def t2(user_name="anonymous"):
    print("hello",user_name)

t2()

# ======================================
# 연습
# 계산 기능 만들기
# 조건 : 인수 값 없을 때 에러 안 보이게 하기

def plus(a=0,b=0):
    print(a+b)

def minus(a=0,b=0):
    print(a-b)

def multiply(a=0,b=0):
    print(a*b)

def divide(a=0,b=1):
    print(a/b)

def power(a=0,b=1):
    print(a**b)


plus(1,2)
minus(6,3)
multiply(4,5)
divide(8,4)
power(3,2)

plus()
minus()
multiply()
divide()
power()

# [7. 반환 값] | Return Values
# return = 함수 바깥으로 값을 내보낸다.
# return 다음 줄은 실행되지 않는다. = 해당 함수를 종료함

def exchange(money):
    return (str(format(money * 1450,',d'))+"원")

def result_text(pay):
    print("이번 달 월급 :",pay)

to_pay = exchange(2000)
result_text(to_pay)

# 설명
# exchange 함수에서 반환된 값을 to_pay라는 변수에 담아
# result_text 함수를 호출할 때 사용한 것.

# [8. 문자열 안에 변수 넣는 방법]

# f"" 안에서 {} 사용
# ex )
my_name = "Lee"
my_age = 12
my_color_eyes = "brown"
print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color!")

# ======================================
# 연습
# 주스 메이커

def make_juice(fruit):
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🧂"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)