numbers=[1,2,3,4,5,6]
r_num=reversed(numbers)

print("reversed_number :",r_num) #주소값 출력
print(next(r_num)) #값 출력시, next()함수 쓸것
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# iterable 객체에 있는 iterator 
# iterable 객체: 반복가능한 객체(list, dict,range) 
# iterator: 값을 차례대로 꺼낼 수 있는 객체
# class:변수와 함수를 같이 묶은 것
# 객체: 메모리구조에 class가 올라간 것 