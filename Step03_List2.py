# list type에 대해서 알아보자

nums = [ 10, 20, 30, 40, 50]
names = [ "kim", "park", "jo", "oh", "choi"]

# list에 들어있는 데이터를 앞에서부터 순서대로 참조하면서 동작을 할 일들이 많이 발생한다
for item in nums:
    print(item)

# names에 들어있는 데이터를 앞에서부터 순서대로 참조하면서 출력
for item in names:
    print("names 를 순서대로 출력중...")
    print(item)

r1 = range(5) # [0, 1, 2, 3, 4]
r2 = range(10) # [0, 1, 2, 3 ... 8, 9]

print(r1)
print(r2)

for item in range(5):
    print(item)

# result2엔 어느값이 ??
result2 = range(len(names))

print("result2 값은", result2)
# 반복문 돌면서 인덱스도 같이 필요해요
for i in range(len(names)):
    print("list의 인덱스와 함께 출력합니다.")
    print(i, names[i])

print("종료합니다.")