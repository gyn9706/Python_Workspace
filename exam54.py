#가변 매개변수 #받는 쪽 변수 하나에 주는 쪽의 변수 개수가 여러개 가능! 
#가변 배개변수는 뒤쪽에 써주기 def f_name(*values,n) (불가x)
def print_n_times(n,*values): 

    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

def print_n_times2(value,n=2): #default(기본값)설정
    for i in range(n):
        print(value) #2번 반복

print_n_times2("안녕",3) #넘어가는 값이 우선 #3번 반복

