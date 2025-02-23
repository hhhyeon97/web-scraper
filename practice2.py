
# Control Flow

# [9. If]

if 10 > 5:
    print("Correct!")

if 10 == 10:
    print("True!")

a = 10
name = "Lee"

if a == 10:
    print("True!")
if name == "Lee":
    print("True!")

# [10. Else & Elif]
# 조건 중 true를 발견하면 종료됨
# ㄴ 뒤 코드는 더 이상 확인하지 않는다.
# else는 다른 조건이 모두 false 일 때 실행될 부분
# elif는 다른 조건 추가하고 싶을 때 사용
# 둘 다 선택 사항임!

password_correct = False

if password_correct:
    print("Here is your money")
else:
    print("Wrong password")

winner = 20

if winner > 10:
    print("Winner is greater than 10")
elif winner < 10:
    print("Winner is less than 10")
else:
    print("Winner is 10")

# [11. And & Or]
# And 연산자는 두 조건이 모두 참이여야 참 반환
# 하나라도 거짓이면 거짓 반환

# Or 연산자는 두 조건 중 하나라도 참이면 참 반환

# input 함수는 하나의 인수만 받는다.
# age = input("How old are you?")
# print("user answer",age)

# type 함수는 변수의 데이터 타입을 확인할 수 있다.
# print(type(age)) # <class 'str'>
# age 변수를 int 형으로 바꿔 주어야 if문으로 숫자와 비교 가능

"""age = int(input("How old are you?"))
if age < 18:
    print("You can't drink.")
elif age >= 18 and age <= 35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
else:
    print("Go ahead!")"""

# [12. Python Standard Library]
# 파이썬은 내장 라이브러리가 매우매우매우 많다.

"""ex )
라이브러리 사용 전
user_choice = int(input("Choose number :"))
pc_choice = 50

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower!")
elif user_choice < pc_choice:
    print("Higher!")
"""

# 값을 랜덤으로 생성하기 위해
# 파이썬 내장 라이브러리 활용
"""
from random import randint # 모듈 안에 있는 함수를 가져오는 코드 예시

user_choice = int(input("Choose number :"))
pc_choice = randint(1,50) # randint(a,b) 지정한 정수 값 범위 안에서 랜덤하게 생성

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! Computer choose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer choose", pc_choice)
"""
# [13. While]

distance = 0

while distance <= 10:
    print("I'm running :",distance,"km")
    distance = distance + 1

# 연습
# 숫자를 맞추면 종료되게 하기

from random import randint

print("★ 숫자 맞추기 게임 ★")

pc_choice = randint(1,100)

playing = True

while playing:
    user_choice = int(input("Choose number(1-100) : "))
    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher")