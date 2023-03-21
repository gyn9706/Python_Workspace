def create_student(name,korean,math,english,science):
    return{
        "name": name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

def students_get_sum(student):
    return student["korean"]+student["math"]+\
            student["english"]+student["science"]

def student_get_average(student):
    return students_get_sum(student)/4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"],
                               students_get_sum(student),
                               student_get_average(student))
    

students=[
    create_student("윤인성",87,98,88,95),
    create_student("연하진",92,98,96,98),
    create_student("구지연",76,96,94,90),
    create_student("나선주",98,92,96,92),
    create_student("윤아린",95,98,98,98),
    create_student("윤명월",64,88,92,92),
] #함수사용: 오타가능성↓ 속도↑ 

print("이름","총점","평균",sep="\t") #seperate 탭으로 분리시켜라! 
for student in students:
    print(student_to_string(student))


"""
for i in students:
    sum=students_get_sum(i)
    avg=student_get_average(i)
    print(i["name"],sum,avg,sep="\t")
"""
"""
for student in students:
    score_sum=student["korean"]+student["math"]+student["english"]+student["science"]
    score_avg=score_sum/4
    print(student["name"],score_sum,score_avg,sep="\t")
    """

