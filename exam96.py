class Animal(object):
    pass

class Dog(Animal):
    def __init__(self,name):
        self.name=name

class Person(): #무조건 Object 상속
    def __init__(self,name):
        self.name=name
        self.pet=None

dog1=Dog("dog1")
person1=Person("홍길동")
person1.pet=dog1 
#person1.pet=dog1.name
print(person1.pet.name)