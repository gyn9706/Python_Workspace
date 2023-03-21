examle_list=["요소A","요소B","요소C"]

print("#단순 출력")
print(examle_list)
print()

print("#enumerate()함수 적용 출력")
print(enumerate(examle_list)) #주소 출력됨
print()

print("#list()함수로 강제 변환 출력")
print(list(enumerate(examle_list))) #[(0,'요소A'), (1,'요소B'), (2,'요소C')] 튜플 ()소괄호로 표현
print()

#참고! 파이썬 자료 처리 형 : 1) 리스트 2) 딕셔너리 3) 튜플

print("#반복문과 조합하기")
for i, value in enumerate(examle_list):
    print("{}번째 요소는 {}입니다.".format(i,value))
