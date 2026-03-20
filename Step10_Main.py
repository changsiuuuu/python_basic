# Step10_main.py

'''
    현재 파일 즉 Step10_main.py에서 run 실행을 하면
    __name__ 은 "__main__"이라는 문자열이 들어있다.
    따라서 __name__을 확인해보면 해당 파일이 main으로 
    실행되었는지 여부를 알 수있다.
    다른곳에서 import 했을때 실행되지 않는 코드 블럭을 만들때
    사용한다.
'''
print("Step10_main.py 실행")
print(__name__)

# 테스트 용도의 클래스 작성하기
class TestClass:
    pass

# 아래의 if문 블럭은 main으로 실행되었을때만 실행된다.(import했을땐 X)
if __name__ == "__main__" :
    print("시작합니다")
    print("작업을하는중")
    print("종료했습니다.")