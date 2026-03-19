# Step08_Input.py

# 콘솔창으로부터 문자열 입력을 받는다.

import ssl

input_msg = input("메세지 입력:")

print(f"입력한 메세지:{input_msg}")

input_name: str = input("이름 입력:")
input_addr: str = input("주소 입력:")

print(f"이름:{input_name} 주소:{input_addr}")
# 문자열로 입력 받은 후
input_age: str = input("나이 입력:")
# 숫자로 변경해서 1을 더한다.
age : int = int(input_age) + 1    # int("19") -> 19 , 연산이 가능한 실제숫자로
                                  # 서른 이라고하면 못바꾸니 에러가뜨는데 처리하는법은 다음에
print(f"당신은 내년에 {age}살 입니다.")