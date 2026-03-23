
# main으로 실행했을때(현재 파일에서 run 했을때) 실행할 code 블럭
if __name__ == "__main__" :

    try :
         # 문자열
        num1_str: str = input("젯수 입력:")
        num2_str: str = input("피젯수 입력:")
        # 입력한 문자열을 숫자로 형변환
        num1 : int = int(num1_str)
        num2 : int = int(num2_str)

        result = num2/num1

        # 결과 출력

        print(f"{num2}를 {num1}으로 나눈 값은 {result}입니다.")
    except ValueError as ve: # ve에는 에러정보가 들어있다.
        print(ve)
        print("숫자 형태로 입력해주세요")
    except ZeroDivisionError as zde:
        print(zde)
        print("0으로 나눌수는 없어요")
   
    # 어떤 중요한 마무리작업을 한다.

    print("중요한 마무리 작업을 합니다.")