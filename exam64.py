"""
file=open("basic.txt","w") #write
file.write("Hello Python Programming...!")

file.close()
"""

#with open("basic.txt","w") as file:  #close() 안해줘도됨!
#    file.write("Hello Python Programming...!")

with open("info.txt","r") as file: #read
    contents=file.read()
print(contents)