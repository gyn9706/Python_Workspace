class Television:
    def __init__(self,channel,volume,on):
        self.channel=channel
        self.volume=volume
        self.on=on
    
    def show(self):
        print(self.channel,self.volume,self.on)
    
    def setChannel(self,channel): #함수이름 set 의미: 저장
        self.channel=channel
    
    def getChannel(self): #함수입력 get 의미: 가져오다
        return self.channel
    
tel=Television(11,30,"on")
tel.show()
tel.setChannel(9)
tel.show()
channel=tel.getChannel()
print(channel)