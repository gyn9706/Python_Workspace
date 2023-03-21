class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name,self.age)

class Student:
    def __init__(self,id):
        self.id=id

    def getId(self):
        return self.id
    
class CollegeStudent(Person,Student):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age) #super()대신, 다이렉트로 지정시, ()없이.하고 인자에 self 넣어주기!! 
        Student.__init__(self,id)

stu=CollegeStudent("kim", 22, "20230310")
stu.show()
print(stu.getId())