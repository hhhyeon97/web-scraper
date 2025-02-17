
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

# 문자열
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

# user_name은 parameter라고 한다.
def say(user_name):
    print("hello",user_name,"!")

# print(name) <- 매개변수는 함수 내에서만 유효함

# Kim, Lee, Park은 argument라고 한다.
say("kim")
say("Lee")
say("Park")

# Parameter는 매개변수로서 함수를 정의할 때 필요한 변수 이름
# Argument는 전달 값으로서 함수를 콜할 때 실제로 넘어가는 값(데이터)