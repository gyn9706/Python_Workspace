#lambda 매개변수 : 리턴값

power=lambda x : x*x
under_3=lambda x : x<3

list_input=[1,2,3,4,5]

output_a=map(power,list_input)
print("# map()함수의 실행 결과:",list(output_a)) #[1,4,9,16,25]

output_b=filter(under_3,list_input)
print("# filter()함수의 실행 결과:",list(output_b)) #[1,2]

