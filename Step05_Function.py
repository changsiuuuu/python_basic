# Step05_Function.py

"""
    Function type

    = 특정시점에 여러줄의 명령어code를 일괄실행하고 싶을 때 사용
    = 함수도 data이다. (변수에 담을 수 있음)
    = 함수 안에 저장된 code를 일괄실행 하는 것을 함수를 call한다고 한다.
    = 함수는 저장된 code를 다 실행하고 나면 call 했던 위치로 실행 흐름이 넘어온다.
    = call 했던 위치로 돌아오면서 어떤 data 를 반드시 가져온다.
"""

def test1():
    print("test1() 호출됨.")

test1()
result1=test1()

# 매개변수가 선언되어 있는 함수.
# 매개변수에 대입할 값을 전달해야지 호출 할 수 있다.
# 매개변수의 이름은 마음대로 지을수 있다..
def test2(arg):
    print("전달 받은 내용:", arg)
    print(f"전달 받은 내용: {arg}")

test2(None)
test2(10)
test2("kim")

# 숫자를 2개 전달받아서 전달 받은 두수의 합을 출력하는 함수
def print_sum(num1: int, num2: int):
    sum=num1+num2
    print(f"{num1} + {num2} = {sum}")

print_sum(10, 20)
print_sum(23, 23)

def print_info(name: str, addr: str):
    print(f"이름은 {name}이고 주소는 {addr}입니다.")

print_info("김구라","노량진")
print_info(addr="행신동", name="해골") # 순서대로 넣지 않고 키워드로 인자를 전달할 수 있다.

def get_sum(num1: int, num2: int):
    sum=num1+num2
    return sum

result2 = get_sum(10, 20) # return이란 예약어가 없으면 기본적으로 None을 가지고 온다

print("종료")