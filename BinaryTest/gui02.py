# BinaryTest/gui02.py


import tkinter as tk
from tkinter import messagebox


def clicked():
    try :
        print("버튼을 클릭했네요")
        # Entry(입력창)에 입력한 문자열 읽어오기
        name=entry.get().strip() # 좌우 공백 제거
        # 입력한 수가 0~255 사이가 아니라면 경고메세지
        if  int(name) < 0 or int(name)> 255 :
            messagebox.showerror("에러", "0~255 사이의 숫자를 입력")
            return
        # text label 수정하기
        result_label.config(text=f"2진수로 변환하면 :{int(name):08b}", fg="blue")
    except ValueError :
        result_label.config(text="올바른 숫자를 입력하세요", fg="red")


if __name__ == "__main__" :
    # root 창 생성
    root = tk.Tk()
    # 제목 설정
    root.title("나의 2진수 변환기")
    # 창의 크기
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text = "10진수를 2진수로 변환")
    #pady = y축 패딩
    label.pack(pady=20)

    # 입력창 만들기
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() # 포커스 주기

    # 버튼
    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgrey")
    btn.pack(pady=15)

    result_label = tk.Label(root, text = "결과는")
    result_label.pack(pady=20)

    # 창이 닫힐때까지 무한 대기
    root.mainloop()