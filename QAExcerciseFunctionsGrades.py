student_name = input("Please enter student's full name: ")
homework_score = int(input("Please enter homework score: "))
assessment_score = int(input("Please enter assessmnent score: "))
final_exam = int(input("Please enter final exam score : "))

def addGrade(homework_score, assessment_score, final_exam):
    addGrade = int((homework_score/25*100 + assessment_score/50*100 + final_exam)/3)
    return addGrade

grade = addGrade (homework_score, assessment_score, final_exam)


if grade < 10:
    print (student_name, "1")
elif grade < 20:
    print (student_name, "2")
elif grade < 30:
    print (student_name, "3")
elif grade < 40:
    print (student_name, "4")
elif grade < 50:
    print (student_name, "5")
elif grade < 60:
    print (student_name, "6")
elif grade < 70:
    print (student_name, "7")
elif grade < 80:
    print (student_name, "8")
else:
    print (student_name, "9")
