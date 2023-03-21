a="Hello Python Programming...!"
a.upper() #대문자
a.lower() #소문자

input_a="""
    안녕하세요
문자열의 함수를 알아봅니다.
"""
print(input_a)
print(input_a.strip()) #양옆의 공백 제거
#lstrip : 왼쪽 공백 제거  #rstrip : 오른쪽 공백 제거

print("TrainA10".isalnum()) #isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인
print("10".isdigit()) #isdigit(): 문자열이 숫자로 인식될 수 있는 것인지 확인

#.의미: 어떤 대상에 접근하여 적용하겠다는 뜻
output_a="안녕하세요".find("안녕")
print(output_a) # 0: 인덱스값
output_b="안녕안녕하세요".rfind("안녕")
print(output_b) # 2: 오른쪽부터 찾아서 만나는 '안'녕의 인덱스값

