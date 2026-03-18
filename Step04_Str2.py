#Step04_Str2.py
'''
    이름과 주소 좋아하는 음식 2가지를 작성해봄
    보면 형식이 다양해서 처리하기 쉽지않다..
    json, xml, yaml ... 이런 형식에 맞춰서

    json은 javascript 객체 표기법을 따르는 문서 형식이다.
    {
        "name":"이창수", 
        "addr":"부산광역시",
        "foods":["메밀소바","치킨"]
    }  --- 중괄호 쓰고 "key":value 숫자는 그냥 적고 "문자열은"
        소문자 true, false 논리값, 또다른 중괄호object, 
        대괄호array, null 빈값
        형식을 잘 맞추면 python java javascript에서 인식..
    
'''
# json 모듈 import 하기.
import json

# info는 str타입이긴 한데 문자열이 특별한 형식(json)을 띄고있다.
info = '''{
    "name":"이창수", 
    "addr":"부산광역시",
    "foods":["메밀소바","치킨"]
}'''
# result 는 str(json형식) 의 문자열이 python의 dict로 변경된 값을 가진다.
result = json.loads(info)

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

# dict에 저장된 데이터를 json 문자열로 변환
# json 문자열 ---- json.loads() ----> python dict
# python dict --- json.dumps() ----> json 문자열

result2 = json.dumps(result)
print("종료.")