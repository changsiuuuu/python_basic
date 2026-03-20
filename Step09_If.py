# Step09_If.py

'''
    임의 숫자를 입력받고 양수면 양수입니다 출력할라면?
'''
input_num: int = int(input("임의의 정수 입력:"))

if input_num > 0 :
    print("입력한 수는 양수입니다.")

# 짝수면 짝수입니다, 홀수면 홀수입니다.

if (input_num) % 2 == 0 :
    print("입력한 수는 짝수입니다.")
else:
    print("입력한 수는 홀수입니다.")
print("종료 합니다.")