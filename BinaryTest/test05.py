# BinaryTest/test05.py

source = "11110000"

print(int(source, 2))

source2 = " 11110003"
# source 문자열 하나하나를 set로 만들어서 "0","1"로만 이루어져 있는지
result1 = set(source).issubset({"0","1"})
result2 = set(source2).issubset({"0","1"})

print(f"{source}이 0과 1로만 이루어져 있는지 여부 {result1}")
print(f"{source2}이 0과 1로만 이루어져 있는지 여부 {result2}")
print(f"{source}가 8자리 초과인지 여부 {len(source) > 8}")