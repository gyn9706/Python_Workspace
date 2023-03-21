class Student:
    def __init__(self,name=None,age=0):
        self.__name=name
        self.__age=age

    def getAge(self):
        return self.__age
    
    def getName(self):
        return self.__name
    
    def setAge(self,age):
        self.__age=age

    def setName(self,name):
        self.__name=name
    
obj=Student("Hong",20)
print(obj.getAge())
obj.setAge(30)
print(obj.getAge())
#다이렉트로 바꾸지말고 이렇게 함수를 통해서 바꾸란 의미(?)
print(obj.getName())