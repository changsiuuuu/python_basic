# Step03_Example.py

"""
    회원 한명의 정보는 번호, 이름, 주소로 이루어져 있음. (dict에 담자.)
    그리고 그러한 회원이 여러명임.
    여러명의 회원 목록을 하나의 묶음으로 순서대로 관리하고싶다. (list에 담자.)
"""

# 3명의 회원정보를 각각 dict에 담고 그 dict를 list에 담는코드

#members = [{"번호":"1", "이름":"강", "주소":"서울"},{"번호":"2", "이름":"호", "주소":"서울2"},{"번호":"3", "이름":"동", "주소":"서울3"}]

mem1 = {"num":1, "name":"김구라", "addr":"노량진"}
mem2 = {"num":2, "name":"해골", "addr":"노량진"}
mem3 = {"num":3, "name":"원숭이", "addr":"동물원"}
# dict 3 개를 list 에 담기
members = [mem1, mem2, mem3]


a = members
b = members[0]
c = members[0]["num"]
d = members[0]["name"]

print("종료합니다")