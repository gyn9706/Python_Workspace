def return_test():
    print("A위치입니다")
    return #함수 종료 
    print("B위치입니다")

value=return_test()
print(value) #None 넘어옴

#값 반환
def return_test2():
    print("A위치입니다")
    return 100 
    print("B위치입니다")

value2=return_test2()
print(value2)

def sum_all(start=0, end=100, step=1):
    output=0

    for i in range(start,end+1,step):
        output+=i
    return output

print("sum_all:",sum_all())
print("sum_all:",sum_all(10)) #start=10
print("sum_all:",sum_all(end=10))
print("sum_all:",sum_all(end=100,step=2))
