def power(item):
    return item*item

def under_3(item):
    return item<3 #True/False 반환

list_input_a=[1,2,3,4,5]

#map()함수 : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성
output_a=map(power,list_input_a)
print("#map()함수의 실행 결과")
print("map(power,list_input_a):",list(output_a))
print()

#filter()함수 : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로, 새로운 리스트를 구성
output_b=filter(under_3,list_input_a)
print("#filter()함수의 실행 결과")
print("filter(under_3,list_input_a):",list(output_b))
print()