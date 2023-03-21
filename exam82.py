class Student:
    def __init__(self,name=None,age=0):
        self.__name=name #__(언더바_두개)가 변수앞에 붙으면 외부에서 변경(접근) 금지
        self.___age=age
#캡슐화: 내부의 데이터 보호 #클래스에 있는 데이터값 노 오픈할 때 사용

obj=Student()
#print(obj.__age)
obj.__age=21
print("obj.__age :",obj.__age) #21로 출력됨,,(?_?)왜그런지모름 파이썬에 문의해야함ㅋㅋㅋ

# obj=Student("홍길동",20)
# obj.__age=21
# print("obj.__age :",obj.__age)
# #print(obj.__name) #AttributeError
# #print(obj.__age)
