# BinaryTest/test01.py

# python에서 2진수 다루기....

# 2진수는 숫자를 만들때 prefix로 0b
num1 = 0b1010 # 10진수로 환산하면 10이된다.

result = num1 + 5
print(result)

#10진수를 2진수로 바꾸고싶다..
num2 = 150
result2 : str = bin(150) # bin()함수 호출하면서 10진수를 넣으면 2진수 숫자가 나온다.
print(result2)

print("------")

line = "abcde12345"

print(line[5:10]) # 5번인덱스 이상, 10번인덱스 미만 문자열 얻어내기
# 위의 result2 문자열에서 0b를 제거하려면 순수 2진수만

print(result2[2:])