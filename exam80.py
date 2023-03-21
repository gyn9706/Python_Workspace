class Car:
    def __init__(self,speed,color,model):
        self.speed=speed
        self.color=color
        self.model=model

    def drive(self):
        self.speed=60
    


car=Car(0,"blue","bmw")

print("자동차 객체를 생성하였습니다.")
print("자동차 속도는:",car.speed)
print("자동차의 색상은:",car.color)
print("자동차의 모델명은:",car.model)

car.drive()
print("자동차의 속도는:",car.speed)