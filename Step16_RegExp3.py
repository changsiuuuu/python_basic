# Step16_RegExp3.py

logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

#logs에서 ERROR or WARN 로그만 찾아서 콘솔창에 출력해보세요


import re

for a in logs :
    if re.search(r"(\[ERROR\])|(\[WARN\])", a) :
        print(a)
