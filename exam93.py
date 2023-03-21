# raise : 의도적으로 에러를 발생시켜야 하는 경우
# 상위 클래스를 설계할 때 하위 클래스에서 반드시 오버라이드하여
# 상세하게 구현해야 하는 함수를 명시하고자 하려면 해당 함수의 내용으로
# raise NotImplementedError(메세지)로 처리한다
import math

class Shape:
    def __init__(self,name):
        self.name=name

    def getArea(self):
        raise NotImplementedError("이것은 추상함수입니다")
        # 추상함수 : 내용이 없는 함수
    
class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius

    def getArea(self):
        return math.pi*self.radius**2

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width=width
        self.height=height

    def getArea(self):
        return self.width*self.height

#shape=Shape("홍길동")
#shape.getArea()

#c=Circle("c",10)
#r=Rectangle("r",10,30)
# print("원의 넓이: ",c.getArea())
# print("직사각형의 넓이: ",r.getArea())

A=[Circle("홍길동",10),Rectangle("이순신",10,10)]
for i in A:
    print(i.getArea())

