class Television:
    serialNumber=0  #클래스 변수(공동사용)

    def __init__(self,channel,volume,on):
        self.channel=channel
        self.volume=volume
        self.on=on
        Television.serialNumber+=1
        self.number=Television.serialNumber

    def show(self):
        print(self.channel,self.volume,self.on,self.number)

myTV=Television(11,10,True)
myTV.show() #self.number=1
myTV.show()
myTV.show()
myTV1=Television(9,15,False)
myTV1.show() #self.number=2
myTV1.show()
myTV1.show()

