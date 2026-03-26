# Step16_RegExp3.py

# list안 어떤 서버의 로그가 들어있음..
logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

#logs에서 ERROR or WARN 로그만 찾아서 콘솔창에 출력해보세요


import re

#for a in logs :
    #if re.search(r"^\[ERROR\]|^\[WARN\]", a) :
        #print(a)

# 첫글자가 W or A or R or N 인지를 검증하는 정규표현식
pattern1 = r"^[WARN]"
# [WARN]으로 시작하는지를 검증하는 정규표현식
pattern2 = r"^\[WARN\]"
# [ERROR]로 시작하는지를 검증하는 정규표현식
pattern3 = r"^\[ERROR\]"
# WARN or ERROR로 시작하는지를 검증하는 정규표현식
pattern4 = r"^(WARN|ERROR)"
## [WARN] or [ERROR]로 시작하는지를 검증하는 정규표현식
pattern = r"^\[(WARN|ERROR)\]"

for tmp in logs :
    # 정규표현식에 매칭되는 문자열이 있다면..
    if re.search(pattern3, tmp):
        print(tmp)

