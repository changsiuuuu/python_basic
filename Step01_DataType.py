# 한줄 주석입니다.

"""
    여기는 여러줄 주석입니다.
    어쩌구 저쩌구...
"""

print("Step01 시작")

# python 의 여러가지 데이터 type에 대해서 알아보자.

# int type
num1 = 10
# num1의 type은 int type, value는 10, 변수 이름은 num1
# float type
num2 = 10.1
# num2의 type은 float type, value는 10.1
# str type
myName = '김구라'
yourName = "해골"
ourName = """
    KT Cloud Infra
    화이팅!
"""
# myName의 type은 str type, value는 김구라


# 순서가 중요한 여러개의 데이터를 관리하고 싶다면 ....
# 내가 좋아하는 음식 목록 3가지를 하나의 변수에 순서대로 담고싶다...
food1="소바"
food2="국밥"
food3="치킨"
foods=["소바", "국밥", "치킨"]

print(foods)


# 순서가 중요치 않지만 여러개의 데이터를 관리하고 싶다면 ...
# 회원 1명의 정보
num =1
name ="김구라"
addr="노량진"

mem1 = {"num":1, "name":"김구라", "addr":"노량진"}
print(mem1)


#foods의 타입은 list type, [ 값1, 값2, 값3]
# mem1의 타입은 dict타입. value는 
# {"key":value, "key2":value2}
#value엔 int float str list dict 타입이 또 들어갈 수 있다.


#순서가 중요치 않은 데이터를 하나의 묶음으로 관리(키값 없이)
mySet = {"빨강사탕","초록사탕","노랑사탕"} #Set type

# 특정 code블럭을 필요한 시점에 일괄 실행하고 싶다...

#함수를 만든다.
def store():
    print("냉장고 문을 연다")
    print("물건을 저장한다.")
    print("냉장고 문을 닫는다")

#필요한 시점에서 함수명()로 실행한다.

store()

returnvalue = store()
#store의 타입은 function type. value는 print("asdas")


print(mySet)
print(myName)

# 어떤 변수를 빈 상태로 만들고 값을 나중에 넣고싶으면 None
a = None
print("어떤 작업을 하고 필요할때 값을 넣는다")
a = "테스트"
print(a)
a = 11
print(a)

#참과 거짓을 나타내는 data type (Bool)
isMan = True
isWoman = False
isDifferent = True
isRun = False
canEat = True
