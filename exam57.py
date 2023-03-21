#튜플 #수정불가 #중요한 데이터 #바꿀수 없을때 사용
tuple_test=(10,20,30)

print(tuple_test)
print(tuple_test[0])
#tuple_test[0]=100 #튜플은 수정 불가 <-> 리스트와 차이점
#print(tuple_test)

[a,b]=[10,20]
print("a={} : b={}".format(a,b))
(c,d)=(10,20)
print("a={} : b={}".format(c,d))