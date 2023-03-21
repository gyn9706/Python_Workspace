class Car:
    def __init__(self,make,model,color,price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price

    def setMake(self,make):
        self.make=make
    
    def getMake(self):
        return self.make
    
    def getDesc(self):
        #return "차량=({},{},{},{})".format(self.make,self.model,self.color,self.price)
        return "차량=("+str(self.make)+","+\
                str(self.model)+","+\
                str(self.color)+","+\
                str(self.price)+")"

class ElectricCar(Car): #상속 #그대로 물려받아 쓰는것 #부모class(Car) -> 자식class(ElectricCar)
    def __init__(self,make,model,color,price,batterySize):
        super().__init__(make,model,color,price) #super():부모 호출 + Car객체생성
        self.batterySize=batterySize

    def SetBatterySize(self,batterySize):
        self.batterySize=batterySize

    def getBatterySize(self):
        return self.batterySize

def main(): 
    myCar=ElectricCar("Tisla","Model S","white","10000",0)
    myCar.setMake("Tesla")
    myCar.SetBatterySize(60)
    print(myCar.getDesc())
    print(myCar.getBatterySize())

main()

#세상의 모든것을 객체로 구현가능하다(?)
#자식으로 객체생성했지만, super()로 자동으로 부모 객체 생성됨