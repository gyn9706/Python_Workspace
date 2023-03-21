def generator_func(x):
    print("첫번째 입력된 값 * 1:")
    x*=1
    yield x 
    print("두번째 입력된 값 * 2:")
    x*=2
    yield x
    print("세번째 입력된 값 * 3:")
    x*=3
    yield x

#for i in generator_func(1):
#    print(i)

y=generator_func(1)
print(next(y)) #yield까지만 출력
print(next(y))
print(next(y))