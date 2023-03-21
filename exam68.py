def test():
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")

output=test() #output에 A지점통과 저장
print("D지점 통과")
a=next(output) #yield까지
print(a) #A지점통과 1 출력

print("E지점 통과")
b=next(output)
print(b)

c=next(output)
print(c)