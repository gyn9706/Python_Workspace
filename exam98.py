class Address:
    def __init__(self,gu,city):
        self.gu=gu
        self.city=city

class Person:
    def __init__(self,name,e_adr):
        self.name=name
        self.e_adr=e_adr

class Contact(Address, Person):
    def __init__(self,name,e_adr,gu,city):
        Address.__init__(self,gu,city)
        Person.__init__(self,name,e_adr)

    def __str__(self):
        return "이름: "+self.name+"\n이메일: "+self.e_adr+\
        "\n주소: "+self.city+"시 "+self.gu+"구"

c=Contact("kim","kim@gmail","jongro","seoul")
print(c.__str__())