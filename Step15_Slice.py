# Step15_Slice.py

'''
    slice의 기본 문법
    [시작 : 끝 : 증감값]
    - 시작은 해당 인덱스 포함
    - 끝은 해당 인덱스 제외
    [1, 2, 3, 4, 5, 6, 7, 8]
    [1 : 6 : 2]
    1(포함)부터 6(제외)까지 2증가, 2 4 6
'''
nums = [10, 20, 30, 40, 50]

print(nums[1:])
print(nums[2:])
print(nums[3:])

print("---------------")

print(nums[:3])
print(nums[:2])
print(nums[:1])

print("---------------")

# 20, 30, 40이 들어있는 리스트를 얻어내려면
print(nums[1:4])

print("---------------")
print(nums[::1])
print(nums[::2])
print(nums[::3])