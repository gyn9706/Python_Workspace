#반복문
for i in range(10): #0~9
    print("{} 반복문 출력".format(i))

print(list(range(10))) # 0~9

array=[1,2,3,4,5]

for element in array:
    print(element)


list_of_list=[[1,2,3],[4,5,6,7],[8,9]] #2차원

for items in list_of_list:
    print(items)

for items in list_of_list:
    for item in items:
        print(items)