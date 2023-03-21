import random

class Dice: 
    def __init__ (self):
        self.__sides_count=6

    def get_sides_count(self):
        return self.__sides_count
    
    def roll(self):
        # random 난수생성범위: 0.0 <= x < 1.0 ==> 0.00000~ 0.999999.....
        return random.randint(1,self.__sides_count) #1~6까지 정수 랜덤숫자 생성 리턴
    
class FraudDice(Dice):
    def __init__(self):
        super().__init__()
    
    def roll(self):
        while True:
            r=super().roll() #부모에 있는 함수호출
            if r>3: 
                return r

fraud=FraudDice()
print(fraud.roll())

