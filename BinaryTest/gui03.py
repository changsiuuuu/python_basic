# BinaryTest/gui03.py


import tkinter as tk
from tkinter import messagebox


def clicked():
    try :
        print("버튼을 클릭했네요")
        # Entry(입력창)에 입력한 문자열 읽어오기
        name=entry.get().strip() # 좌우 공백 제거
        # 빈칸
        if name == "":
            result_label.config(text="올바른 숫자를 입력하세요", fg="red")
            return
        # 숫자인지 검사
        if not name.isdigit():
            result_label.config(text="올바른 숫자를 입력하세요", fg="red")
            return
        # 입력한 수가 0과 1로만 이루어져 있는지 검사
        if  not set(name).issubset({"0","1"}) :
            messagebox.showerror("에러", "0과 1만 입력")
            return
        # 8자리를 초과하는지 검사
        if len(name) > 8:
            messagebox.showerror("에러", "8자리 까지만 입력")
            return
        # text label 수정하기
        result_label.config(text=f"10진수로 변환하면 :{int(name, 2)}", fg="blue")
    except ValueError :
        result_label.config(text="올바른 숫자를 입력하세요", fg="red")


if __name__ == "__main__" :
    # root 창 생성
    root = tk.Tk()
    # 제목 설정
    root.title("나의 10진수 변환기")
    # 창의 크기
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text = "2진수를 10진수로 변환")
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