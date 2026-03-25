# Step16_RegExp.py

'''
    정규표현식 (Regular Expression)에 대해서 알아보기...
'''

# 우리는 어떤 문자열을 검증하거나 혹은 특정 문자열에서 원하는 단어나 기호를 찾아야 할 때가 있다.

# 아이디적을때 한글은안되고 숫자가 있어야하고 이런걸 제한걸때

import re


data :str = "apple, banana, cherry"
# data에 a는 철자가 있는지, 공백이 있는지 이런걸...

# 'a'라는 정규표현식에 매칭되는 모든 문자열을 찾아서 list에 담아서 리턴한다.
result = re.findall(r"a", data)

print(result)

# 대상문자열 2
text : str = "Contact: 010-1111-2222입니다"
# 전화번호만 뛱 빼내서 사용하고싶음..
# re.Match객체를 얻어낸다.
m_obj = re.search(r"010-[0-9]{4}-[0-9]{4}", text)

# 없으면 None, 있으면 re.match 객체의 참조값
print(m_obj) # 문자열이아님...
# .group()를 호출하면 매칭되는 문자열이 리턴된다.
print(m_obj.group())