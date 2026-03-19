# yaml 형식의 문자열

# yaml 문자열을 다루기위해 외부 모듈을 pip(python package manager) 로 설치 후 import 한다.

import yaml

info = """
name: 이창수
addr: 부산광역시
foods:
  - 메밀소바
  - 치킨
isMan: true
body:
  weight: 75
  height: 174
"""

# 검색 혹은 ai 의 도움을 받아서 info에 들어있는 문자열을 dict type으로 바꾸기.
# dict에 들어있는 내용을 확인하고 다시 yaml 문자열 형식으로 변환하기.

#yaml 형식의 문자열을 safe_load() 로딩해서 dict type으로 변경
result = yaml.safe_load(info)
print(result)
print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])
print(result["body"]["weight"])
print(result["body"]["height"])

# dict type result를 다시 yaml형식으로 변환하는 dump()
result2 = yaml.dump(result, allow_unicode=True, sort_keys=False)
print(result2)
print(type(result))
print(type(result2))
print("종료")