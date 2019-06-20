students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


# def var_args(name, *args):
#    print(name, args)


# def var_args(name, **kwargs):
#    print(kwargs["description"], kwargs["Feedback"], kwargs["isTrue"])


student_list = get_students_titlecase()


userInput = input("Do you want to add new student?").lower()

while userInput == 'yes' or userInput == 'y':
    student_name = input("Enter student name:")
    student_id = input("Enter student ID:")
    add_student(student_name, student_id)
    print_students_titlecase()
    userInput = input("Do you want to add new student?").lower()
    if userInput == 'yes' or userInput == 'y':
        continue
    else:
        break

# add_student(name="Mark", student_id=15)

# print("Hello", "World", 3, None, "Something")

# var_args("Mark", "Love", None, "Hello", True)
# var_args("Mark", description="Love python", Feedback=None, isTrue=True)
