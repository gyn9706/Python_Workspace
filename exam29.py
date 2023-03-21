numbers=[1,2,3,4,5,6,7,8,9]

# 짝수 번째 요소의 값을 제곱한다 
for i in range(0,len(numbers)//2): #0~3
    j=i+i+1
    numbers[j]*=numbers[j] #numbers[j]=numbers[j]**2
    print(f"i={i},j={j}") #f-string ver3.6이후
print(numbers)

"""
i=0, j=1
i=1, j=3
i=2, j=5
i=3, j=7
[1,4,3,16,5,36,7,64,9]
"""

"""
for i in range(0,len(numbers)): #0~8
    if i<4:
        j=i+i+1
        numbers[j]*=numbers[j]
        print("i={},j={}".format(i,j))
print(numbers)


for i in range(0,len(numbers)): #0~8
    if (i+1)%2==0:
        numbers[i]*=numbers[i]
print(numbers)
"""