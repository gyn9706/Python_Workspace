# input()함수 명령 프롬프트에서 사용자로부터 데이터 입력받을 때 사용
# 입력되는 데이터는 문자로 처리된다
string=input("인사말을 입력하세요 :")
print(string)

number=input("숫자를 입력하세요 :")
print(type(number))
#print(number+100) #Type Error

#int()함수: 문자열을 int자료형으로 변환
#float()함수: 문자열을 float자료형으로 변환
string_a=input("입력A> ")
int_a=int(string_a)

string_b=input("입력B> ")
int_b=int(string_b)

print("문자열 자료:",string_a+string_b)
print("숫자 자료:",int_a+int_b)