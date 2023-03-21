import time
number=0

target_tick=time.time()+5 #초단위 시간계산
while time.time() < target_tick: #5초동안
    number+=1

print("5초 동안 {}번 반복했습니다.".format(number)) 