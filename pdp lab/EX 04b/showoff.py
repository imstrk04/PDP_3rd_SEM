def ShowOff(**kwargs):
    name = kwargs.get("name", "")
    marks = kwargs.get("marks", 0)
    subject = kwargs.get("subject", "")
    teacher = kwargs.get("teacher", "")

    if marks > 60:
        print(f"{name}'s marks: {marks}")
    else:
        print(f"{name}'s subject: {subject}, Teacher: {teacher}")

student1_info = {"name": "Aarav", "marks": 75}
student2_info = {"name": "Aditi", "subject": "Math", "teacher": "Mr. Sharma"}
student3_info = {"name": "Amit", "marks": 55}
student4_info = {"name": "Deepika", "subject": "Science", "teacher": "Mrs. Verma"}
student5_info = {"name": "Gaurav", "marks": 80}

students_info = [student1_info, student2_info, student3_info, student4_info, student5_info]
for student_info in students_info:
    ShowOff(**student_info)