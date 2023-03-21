"""
try:
    예외가 발생할 가능성이 있는 구문
execpt 예외의 종류 as 예외 객체를 활용할 변수 이름
    예외가 발생했을 때 실행할 구문
"""

try:
    number_input_a=int(input("정수 입력>"))
    print("원의 반지름:",number_input_a)
    print("원의 둘레:",2*3.14*number_input_a)
    print("원의 넓이:",3.14*number_input_a**2)
except Exception as exception: #Exception: 모든 에러 #ValueError: 타입 다른값 입력시 에러
    print("type(exception):",type(exception))
    print("exception:",exception)

#부모class:상속해줌 -> Exception 
    #자식class:상속받음 -> ValueError 외 다른 에러들 
    #부모class를 써주면 그에 속한 자식class모두 커버가능! 
    #에러 종류모를땐 그냥 Exception으로 대체가능!