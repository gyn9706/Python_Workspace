array=[]
#list 거듭제곱

for i in range(0,20,2):
    #print("i=",i)
    array.append(i*i)
print(array)

array=[i*i for i in range(0,20,2)] #list comprehension
print(array)

#초콜릿과 같지않으면 array의 요소 fruit를 fruit에 저장후 list output출력
array=["사과","자두","초콜릿","바나나","체리"]
output=[fruit for fruit in array if fruit != "초콜릿"] 
print(output)