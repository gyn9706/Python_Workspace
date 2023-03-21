list_e=[52,273,103,32,275,1,7]
list_e.sort() #기본 오름차순 정렬
print(list_e) 

list_e.sort(reverse=True) #역순
print(list_e)

#in 연산자: 특정값이 리스트 내부에 있는지 확인
print(273 in list_e) #true
print(100 in list_e) #false
#not in 연산자: 특정값이 리스트 내부에 없는지 확인
print(273 not in list_e) #false
print(100 not in list_e) #true