a=range(5)
print(a) #range(0,5)
b=list(range(5))
print(b) #[0,1,2,3,4]
b=list(range(0,5))
print(b) #[0,1,2,3,4]
b=list(range(5,10))
print(b) #[5,6,7,8,9]
c=list(range(0,10,2)) #0~9까지 2씩 증가
print(c) #[0,2,4,6,8]
c=range(0,10+1)
print(c) #range(0,11)
c=list(range(0,10+1)) # +,-,*,//,% 가능 but /불가: 실수라서 즉, 실수 연산 제외!
print(c) #[0,1,2,3,4,5,6,7,8,9,10]
