#int("안녕하세요") #ValueError : 문자열을 int나 double로 캐스팅불가
#float("안녕하세요")

number=int("12345")
number+=10;
print(number)

number=int(52.123)
print(number)

#number=int("52.123")
#print(number) #ValueError #문자열->숫자 같은타입으로 바꿔야함

number2=float("52.123")
print(number2) 

output_a=str(52)
output_b=str(52.273)
print(type(output_a),output_a)
print(type(output_b),output_b)
