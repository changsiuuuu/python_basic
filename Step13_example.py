# Step13_example.py

info : dict = {
    "num":1,
    "name":"김구라",
    "body":{
        "height": 180,
        "weight": 80
    },
    "hobby":["피아노", "당구", "프로그래밍"]
}

# dict안에 num키값 int, name키값의 str, body키값으로 dict, hobby라는 키값으로 list

'''
     위의 info 안에 들어 있는 데이터를 이용해서 아래와 같은 형식의 문자열을 출력하기

     번호 : 1
     이름 : 김구라
     키 : 180 cm
     몸무게 : 80 kg
     취미 : 
        - 피아노  
        - 당구  
        - 프로그래밍
'''

from jinja2 import Template

my_template = """
    번호 : {{ num }}
    이름 : {{ name }}
    키 : {{ body.height }} cm
    몸무게 : {{ body.weight }} kg
    취미 : {% for hobby in hobby %}
    - {{ hobby }}
    {% endfor %}
"""
# Template 객체 생성
temp : Template = Template(my_template)
# Template 객체의 render() 메소드를 이용하여 랜더링한다..
result : str = temp.render(info)
print(result)