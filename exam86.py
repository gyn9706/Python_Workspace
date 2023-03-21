class Dog:
    kind="Bulldog"
    def __init__(self,name,age=0):
        self.name=name
        self.age=age

a=Dog("Baduk",2) #둘다 무조건 불독임 #클래스변수 공용이라서
b=Dog("Marry",3)

print(a.kind,a.name,a.age)
print(b.kind,b.name,b.age)

print(Dog.kind) #c언어에서 static과 동일 #클래스변수는 객체생성 없이 클래스 이름으로 바로접근가능

