# str type 에 대해서 알아보자 ( 중중요 )

# 양쪽에 공백이 포함되거나 포함될 가능성이 있는 문자열
# 만일 공백을 제거하고 싶다면 ...
text = "     Cloud Infra        "
result1 = text.strip()

myIp = "192.168.0.2"
# 숫자 하나하나를 .으로 분리하기 분리해서 list에 담고싶어
result2 = myIp.split(".")
# join으로 다시 합치기
result3 = ".".join(result2)

# 특정 문자열을 찾아서 대체하기
result4 = "hello mimi!".replace("mi","ma")

result5 = "python".upper()
result6 = "PYTHON".lower()

# 이런기능들이 있다....
print("제거합니다")