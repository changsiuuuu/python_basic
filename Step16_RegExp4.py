# Step16_RegExp4.py


import re


if __name__ == "__main__" :
    # 임의의 문자열을 입력받는다.
    user_id = input("아이디를 입력하세요(영문 대소문자, 숫자만 가능):")

    # 입력한 문자열을 검증해서 조건에 맞으면 가입되었습니다. 맞지않으면 사용할 수 없는 아이디입니다 출력
    # 프로그래밍을 해보자.
    input_id = re.search(r'^[A-Za-z0-9]+$', user_id)
    if input_id :
        print(f"{input_id.group()}로 가입되었습니다.")
    else :
        print("사용할 수 없는 아이디입니다.")
