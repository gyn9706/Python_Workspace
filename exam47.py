example_dictionary={
    "키A":"값A",
    "키B":"값B",
    "키C":"값C",
}

print("# 딕셔너리의 items()함수")
print("items():",example_dictionary.items()) #list구조로 변환되면서 튜플형으로 나옴
print()

print("# 딕셔너리 items()함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}]={}".format(key,element))