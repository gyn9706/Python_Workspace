numbers=[273,103,5,32,65,9,72,800,99]

#for, if 사용 100이상의 숫자 출력
for i in numbers:
    if i>=100:
        print("100 이상의 수:",i)
print()
#짝수, 홀수
for number in numbers:
    if number%2==0:
        print(number,": 짝수")
    else:
        print(number,": 홀수")
print()

#숫자 길이(자릿수) 계산 1(한자리) 12(두자리) 123(세자리)
"""
for num in numbers:
    if len(str(num))==1:
        print(num,": 한자리")
    elif len(str(num))==2:
        print(num,": 두자리")
    else: 
        print(num,": 세자리")
"""

for num in numbers:
    print(num,"은",len(str(num)),"자릿수입니다")
