dictionary={}

print("요소 추가 이전 :",dictionary)

# 키와 값을 쌍으로 줘야함
dictionary["name"]="새로운 이름"
dictionary["head"]="새로운 정신"
dictionary["body"]="새로운 몸"
print("요소 추가 이후 :",dictionary)

del dictionary["body"]
print("요소 제거 이후 :",dictionary)

#print(dictionary["body"]) #KeyError