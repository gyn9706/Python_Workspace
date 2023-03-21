list_a=[1,2,3]

print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a) # 1 2 3 4 5
print()

print("#리스트 중간에 요소 추가하기")
list_a.insert(0,10) #0번째에 10 추가 #(삽입될 위치,추가할 요소) #주의: 덮어쓰기 아니고 데이터들이 이동!
print(list_a) # 10 1 2 3 4 5

list_a.extend([6,7,8])
print(list_a) # 10 1 2 3 4 5 6 7 8

del list_a[0] #삭제
print(list_a) # 1 2 3 4 5 6 7 8

list_a.pop(2) #제거 #3이 스택에서 팝!(out)됨
print("pop(2):",list_a) # 1 2 4 5 6 7 8

del list_a[3:7] #index값 3번째부터~(7-1)번째까지 삭제
print(list_a) # 1 2 4

del list_a[:3]
print(list_a) # []

list_a.append(1)
list_a.append(2)
list_a.append(2)
print(list_a) # 1 2 2
print()

list_a.remove(2) #1 2 #값으로 제거 (index값 아님)
list_a.remove(1) #2
print(list_a)

list_a.clear()
print(list_a) #[]
