class MyTime:
    def __init__(self,hour,minute,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second) # 출력할 형식 % (출력할 데이터 값)
    
time=MyTime(1,55)
print(time)