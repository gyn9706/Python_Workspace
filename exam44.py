#1*99,2*98,3*97,...,98*2,99*1  최대값이 되는 경우?
max_value=0
a=0
b=0

for i in range(1,100//2+1):
    j=100-i
    current=i*j
    
    if max_value<current:
        max_value=current
        a=i
        b=j
print(f"최대가 되는 경우 : {i}*{j}={max_value}")

"""
for a in range(1,100):
    b=100-a 
    if (a*b) > (a-1)*(b+1):
        max_value=a*b

print(max_value)
"""