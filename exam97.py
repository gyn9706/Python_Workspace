class Person:
    def __init__(self,name,number):
        self.name=name
        self.number=number

class Student(Person):
    UNDERGRADUATE=0
    POSTGRADUATE=1

    def __init__(self,name,number,studentType): #생성자함수
        super().__init__(name,number)
        self.studentType=studentType
        self.gpa=0 #init함수에서 변수 생성! 즉, 객체생성시 같이 생성됨
        self.classes=[] #init함수에서 변수 생성! 즉, 객체생성시 같이 생성됨

    def enrollCourse(self,course):
        self.classes.append(course)

    def __str__(self): #__함수명__: 개발자들이 만들어준 함수
        return "\n이름="+self.name+"\n주민번호="+self.number+\
        "\n수강과목="+str(self.classes)+"\n평점="+str(self.gpa)
    
class Teacher(Person):
    def __init__(self,name,number):
        super().__init__(name,number) #super()괄호 빼먹지말자
        self.courses=[]
        self.salary=3000000
    
    def assignTeaching(self,course):
        self.courses.append(course)

    def __str__(self): 
        return "\n이름="+self.name+"\n주민번호="+self.number+\
        "\n강의과목="+str(self.courses)+"\n월급="+str(self.salary)
    
hong=Student("홍길동","12345678",Student.UNDERGRADUATE)
hong.enrollCourse("자료구조")
print(hong)

kim=Teacher("김철수","1234567890")
kim.assignTeaching("Python")
print(kim)