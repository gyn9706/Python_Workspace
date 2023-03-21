i=0
while i<10:
    print("{}번째 반복입니다.".format(i))
    i+=1

list_test=[1,2,1,2]
value=2

while value in list_test: # list_test 내부에 value가 있다면
    list_test.remove(value)

print(list_test)
