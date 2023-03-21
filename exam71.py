list_input_a=["52","273","32","스파이","103"]

list_number=[]

#try except else finally 쓸 때 순서 꼭 맞춰주기/ 조합은 맘대로
for item in list_input_a:
    try:
        #예외가 발생할 가능성이 있는 코드
        float(item)
        list_number.append(item)
    except:
        #예외가 발생했을 때 실행할 코드
        pass 
    else:
        print("예외가 발생하지 않았을 때 실행할 코드")
    finally:
        print("finally는 예외 발생과 상관없이 무조건 실행합니다.")

print("{}내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))