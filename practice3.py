
# Data Structures | 자료 구조
# 데이터를 구조화하고 싶을 때 사용한다.
# 여기선 list, tuple, dictionary를 배울 예정

# [14. Methods]

# 메서드
# 변수 뒤에 .을 찍어보면 다양한 기능들을 사용할 수 있음
# print, input 등은 함수임 -> 데이터에 결합된 형태가 아닌!
# 💡 메서드는 데이터와 결합/연결된 function이다.
# ex ) 다양한 문자열 관련 메서드 참고 https://docs.python.org/ko/3.13/library/stdtypes.html#text-sequence-type-str

# ex )
"""name = "lee"
print(name.upper()) # LEE
print(name.capitalize()) # Lee
print(name.startswith("a")) # False
print(name.replace("e","⚡")) # l⚡⚡
print(name.endswith("e")) # True
print("kim".upper()) # KIM"""


# [15. Lists]
# list 
# 대괄호 사용
# 쉼표로 데이터 구분
# mutable(변경가능)
# 리스트 관련 참고 https://wikidocs.net/14

# 리스트 생성
"""days_of_week = ["Mon","Tue","Wed","Thur","Fri"]

print(days_of_week) # ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']

# 리스트 관련 메서드 ex )
print(days_of_week.count("Wed")) # 1
# days_of_week.clear()
# print(days_of_week) # []
# days_of_week.reverse()
# print(days_of_week) # ['Fri', 'Thur', 'Wed', 'Tue', 'Mon']
days_of_week.append("Sat") 
print(days_of_week) # ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
days_of_week.append("Sun")
print(days_of_week) # ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# 인덱스로 아이템 접근 가능 / 인덱스는 0부터 시작한다. / 거꾸로도 접근 가능
print(days_of_week[0]) # Mon
days_of_week.remove("Fri")
print(days_of_week) # ['Mon', 'Tue', 'Wed', 'Thur', 'Sat', 'Sun']

print("===================")"""

# [16. Tuples]
# Tuple
# 소괄호 사용
# 리스트와 다른 점 : 튜플은 불변성을 가진다.(immutable)
# 변경 불가 -> 쓸 수 있는 메서드도 몇 가지 없음

"""days = ("Mon","Tue","Wed")
print(days.count("Mon")) # 1
print(days.index("Wed")) # 2
print(days[0]) # Mon
print(days[-1]) # Wed"""


# 리스트는 변경해도 될 데이터에, 
# 튜플은 변경하고 싶지 않은 데이터에
# 적절히 용도에 따라 사용하면 된다.


# [17. Dicts]
# Dictionary
# 중괄호 사용
# mutable
# Key:Value 형태 (키-값 쌍 형태)

"""player = {
    "name":"Lee",
    "age":12,
    "alive":True,
    "fav_food":["🥞","🍙"]
}

print(player) # {'name': 'Lee', 'age': 12, 'alive': True}
print(player.get("age")) # 12
print(player.get("fav_food")) # ['🥞', '🍙']
print(player["name"]) # Lee

print(player.keys()) # dict_keys(['name', 'age', 'alive', 'fav_food'])
print(player.values()) # dict_values(['Lee', 12, True, ['🥞', '🍙']])

# 데이터 삭제
print(player)
player.pop("age")
print(player)

# 데이터 추가
print(player)
player["xp"] = 1500
print(player)

# player 딕셔너리 안에 있는 fav_food 리스트에
# 리스트 메서드 중 하나인 append 사용한 예시
player["fav_food"].append("🍜")

# 두 출력 방법은 결과가 같다.
print(player["fav_food"])
print(player.get("fav_food"))"""

# 연습
"""user = {
    "name":"Lee",
    "id":"lee123",
    "age":20,
    "email":"lee@naver.com",
    "phone":"010-1111-2222"
}

print(user) # {'name': 'Lee', 'id': 'lee123', 'age': 20, 'email': 'lee@naver.com', 'phone': '010-1111-2222'}
print(user["name"]) # Lee
user.pop("age")
print(user) # {'name': 'Lee', 'id': 'lee123', 'email': 'lee@naver.com', 'phone': '010-1111-2222'} 
user["address"] = ["서울시","마포구","망원동"]
print(user) # {'name': 'Lee', 'id': 'lee123', 'email': 'lee@naver.com', 'phone': '010-1111-2222', 'address': ['서울시', '마포구', '망원동']}
print(user["address"]) # ['서울시', '마포구', '망원동']
print(user["address"][0]) # 서울시"""


# [18. For Loops]

# (튜플이나 리스트 만들 때 이름을 복수형으로 사용하는 관습이 있다.)
websites = (
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com",
    "instagram.com"
)

# ex ) 튜플의 각각의 item에 프린트 코드를 실행시킴
# 리스트도 똑같이 가능!

for site in websites:
    print("hello")

# 💡 여기서 site는 튜플 안에 있는 각각의 아이템이다.

# 현재 처리중인 item이 무엇인지 알려면 ?!

for site in websites:
    print("site is equals to", site)


# [19. URL Formatting]