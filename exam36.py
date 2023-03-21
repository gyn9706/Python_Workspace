array=[273,32,103,57,52]

for element in array:
    print(element)

print(array)

print(len(array)) #5

#for i in len(array): (x)
for i in range(len(array)):
    print("{}번째 반복 : {}".format(i, array[i]))

for i in range(4,0-1,-1):
    print(i) #4,3,2,1,0

for i in reversed(range(5)):
    print(i)
