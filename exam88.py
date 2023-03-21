class Animal:
    def __init__(self,age=0):
        self.__age=age

    def eat(self):
        print("동물이 먹고 있습니다.")

class Dog(Animal):
    def __init__(self,age=0,name=""):
        super().__init__(3) #age=3넘겨줌 
        self.name=name

d=Dog() #자식객체생성
print(d.age) #self.age=age일 땐 3출력 #self.__age=age 이후엔 AttributeError
e=Animal() #부모객체생성 가능
print(e.age) #0출력
