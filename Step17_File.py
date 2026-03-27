# Step17_File.py

import os


if __name__ == "__main__" :
    # 현재 작업 폴더의 경로 os.getcwd()
    print(os.getcwd())
    # 파일 구분자 (윈도우는 역슬래시, linux는 슬래시를 얻어낸다.)
    print(os.sep)
    r'''
        현재 memo.txt파일은 C:\playground\python_basic\memo.txt
        의 경로에 존재한다. 해당 경로를 문자열로 만들어보면...
    '''
    # 읽어올 파일의 절대경로 구성
    # os.path.join() -> window에선 역슬로, linux에선 슬래시
    # 로 조합한다.
    path : str = os.path.join(os.getcwd(),"memo.txt")
    print(path)

    # with 구문을 이용해서 path 경로에 있는 text 파일을 읽기(r) 전용으로 열어서 f 라는 별칭으로 사용한다
    with open(path, "r", encoding="utf-8") as f:
        # 파일에서 문자열 읽기
        result = f.read()
        print("--- memo.txt 파일의 내용 ---")
        print(result)
