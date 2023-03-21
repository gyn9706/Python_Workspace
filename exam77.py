class Counter:
    def __init__(self,initValue=0):
        self.count=initValue
    
    def increment(self):
        self.count+=1

a=Counter() #__init__() 호출 #힙에 만들어진 Counter()를 스택의 변수에 (주소)저장해야 (값을 주어)사용가능!
b=Counter(100)

a.increment()
print("카운터의 값=",a.count) #1

b.increment()
print("카운터의 값=",b.count) #101

#사람이더라도 각자 다르게 생김 
# 즉, 스택의 변수 a, b 각각 힙에 구성은 같지만 저장된 값이 다른Counter Counter 공간 따로 가지고 있음
