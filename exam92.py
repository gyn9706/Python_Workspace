class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary #월급

    def getSalary(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self,name, salary, bonus):
        super().__init__(name, salary)
        self.bonus=bonus

    def getSalary(self):
        salary=super().getSalary() #괄호 빼먹지 말자!! sumper()괄호.함수()괄호!! 
        return salary+self.bonus
    
    def __str__(self): #__repr__ 과 기능 동일 
        return "이름:"+self.name+"; 월급:"+str(self.getSalary())+\
        "; 보너스:"+str(self.bonus)


kim=Manager("김철수",2000000,100000)
#print("이름: {} 월급: {} 보너스: {}".format(kim.name, kim.getSalary(), kim.bonus))
print(f"이름: {kim.name} 월급: {kim.getSalary()} 보너스: {kim.bonus}")
print(kim.__str__())