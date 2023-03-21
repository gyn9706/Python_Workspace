#끝자리로 짝수와 홀수 구분
number=input("<정수 입력>")

last_character=number[-1]
last_number=int(last_character)

"""
#\로 이어졌음을 알려줌
if last_number ==0 \
    or last_number ==2 \
    or last_number ==4 \
    or last_number ==6 \
    or last_number ==8:
    print("짝수입니다")
    
if last_number ==1 \
    or last_number ==3 \
    or last_number ==5 \
    or last_number ==7 \
    or last_number ==9:
    print("홀수입니다")
"""

if last_number % 2 ==0:
    print("{}은 짝수입니다".format(number))
else :
    print("{}은 홀수입니다".format(number))
