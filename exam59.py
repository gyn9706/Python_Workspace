a,b=10,20

print("# 교환 전 값")
print("a:",a)
print("b:",b)
print()

a,b=b,a

print("# 교환 후 값")
print("a:",a)
print("b:",b)
print()

def test():
    return (10,2) #c언어에선 포인터없이 리턴값 여러개 불가 #파이썬은 가능

a,b=test() 
print("a:",a)
print("b:",b)
print()