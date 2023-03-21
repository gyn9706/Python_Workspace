# 딕셔너리(dictionary) : 키를 기반으로 값을 저장하는 것 / 리스트[]는 인덱스 기반

dictionary={
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin": "필리핀"
}

print("name:",dictionary["name"])
print("type:",dictionary["type"])
print("ingredient:",*dictionary["ingredient"])
print("origin:",dictionary["origin"])
print()

dictionary["name"]="8D 건조 망고" #변경
print("name:",dictionary["name"])
print("ingredient:",dictionary["ingredient"][1]) #설탕
print(dictionary)
dictionary["price"]=5000 #추가
print(dictionary)

del dictionary["ingredient"] #삭제
print(dictionary) 