# Step17_File2.py

import os

if __name__ == "__main__" :
    letter_path = os.path.join(os.getcwd(), "my_letter.txt")
    
    with open(letter_path, "r", encoding="utf-8") as f :
        #문자열을 한줄씩 읽어서 콘솔에 출력
        #프린트라는 함수 자체도 개행기호를 출력한다..
        #그래서 원본에 개행기호가 있어서 한줄 점프해서 나옴
        print(f.readline())
        print(f.readline())
        print(f.readline())
        print(f.readline().strip()) #좌우 공백과 개행기호를 없애는 .strip()
        print(f.readline().strip())
        print(f.readline().strip())
    print("-------------반복문으로 처리------------")

    with open(letter_path, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())