# Step06_Tuple.py

'''
    - tuple
    list type과 유사
    읽기 전용 ( 수정, 삭제안됨.)
    기능이 적어 처리속도가 빠른 장점...

    만드는법

    (value1, value2, value3) list:  [ value1, value2, value3] 튜플도 인덱스가붙음
'''

# "one", "two", "three" 3개의 str type 데이터를 tuple에 순서대로 담고
# 그 객체의 참조값을 tuple type tuple1이라는 변수에 담기
tuple1 : tuple = ("one", "two", "three")
result1 = tuple1[0]
result2 = tuple1[1]
result3 = tuple1[2]

# readonly이기 때문에 수정 삭제가 불가능하다
# del tuple1[0]
# tuple1.remove(0)
# tuple1[0] = " xxx "

# 방 1개의 tuple type을 만들때는 주의
tuple2 = ("김구라",) # ,가 필요하다...

# 괄호 없는 튜플 생성
tuple3 = 10, 20, 30

# tuple 에 저장되 값을 여러 변수에 나누어 담기
a, b, c = tuple3

# 두 변수에 있는 값을 서로 바꾸려면 
first = "girl"
second = "boy"
'''
tmp = first
first = second
second = tmp
'''
# 위 3줄을 이렇게 해결한다.
first, second = second, first

print("종료합니다")