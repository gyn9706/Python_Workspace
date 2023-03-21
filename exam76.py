class Student: #클래스 첫글자는 대문자
    # 생성자 : 클래스 이름과 같은 함수 -> 반드시 존재!, self:자기자신(Student)
    def __init__(self,name,korean,math,english,science): #->생성자: 클래스 초기화 #(매개변수들:외부에서가져옴)
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

    def get_sum(self): #self.변수: class의 변수를 가져올때 사용
        return self.korean+self.math+self.english+self.science
    
    def get_average(self): #parameter(매개변수): 받는값 / argument(인자값): 주는값 
        return self.get_sum()/4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())
    

students=[
    Student("윤인성",87,98,88,95), #__init__(생성자)호출방법: Student() 클래스이름과 동일함 #객체생성!
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92)
    ]

print("이름","총점","평균",sep="\t")
for student in students:
    print(student.to_string())

#number=['a','b','c','d']
#number[0] ==> 'a'
#number[1] ==> 'b'

#ctrl+k+c 주석생김!
# # students[0].name #윤인성
# # students[0].korean #87
# # students[0].math #98
# # students[0].english #88
# # students[0].science #95
