import math

#자식 클래스의 함수가 부모 클래스의 함수를 오버라이드(재정의)한다 : 함수명이 같을 때 자식 함수가 실행됨!!

class Shape:
    #def __init__(self): # 기본 생성자: 매개변수x, 하는일 x =>자동 init실행!
    #    pass

    def draw(self):
        print("draw()가 호출됨")

    def get_area(self):
        print("get_area()가 호출됨")

class Circle(Shape):
    def __init__(self,radius=0):
        #super().__init__() : 자동실행 but 부모클래스가 기본생성자일때!
        self.radius=radius

    def draw(self):
        super().draw() #부모함수 쓰고싶을때 사용
        return ("원을 그립니다.")
    
    def get_area(self):
        return math.pi*self.radius**2
    
c=Circle(10) # 객체 생성
print(c.draw())
print("원의 면적:",c.get_area())