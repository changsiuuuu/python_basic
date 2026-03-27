# Step17_File2.py

import os


if __name__ == "__main__" :
    
    # 새로운 파일을 만들어서 문자열을 파일에 출력하기

    letter_path = os.path.join(os.getcwd(), "my_letter.txt")

    with open(letter_path, "w", encoding="utf-8") as f:
        f.write("to my friend\n")
        f.write("하이용")
        f.write("\n바이용\n")

    # 파일을 열어서 문자열 추가하기 append mode
    # 기존을 유지하면서 추가.
    with open(letter_path, "a", encoding="utf-8") as f:
        f.write("어쩌구.. 저쩌구..\n")
        f.write("어쩌구.. 저쩌구..\n")
        f.write("어쩌구.. 저쩌구..\n")
        f.write("어쩌구.. 저쩌구..\n")
        f.write("어쩌구.. 저쩌구..\n")
        f.write("어쩌구.. 저쩌구..\n")
        f.write("어쩌구.. 저쩌구..\n")
        f.write("어쩌구.. 저쩌구..\n")
        

    print("my_letter.txt 파일 생성 및 쓰기 완")
