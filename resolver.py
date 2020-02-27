# Student and class lists
students = []
classes = []

# Student and class ID starts with
last_student_id = 1234455
last_class_id = 1122333


def student_with_id(_, info, _id):
    for student in students:
        if student['id'] == _id:
            print(student)
            return student


def class_with_id(_, info, _id):
    for classs in classes:
        if classs['id'] == _id:
            return classs


def add_student(_, info, name):
    global last_student_id
    last_student_id += 1
    new_student = {'id': last_student_id, 'name': name}
    students.append(new_student)
    return new_student


def add_class(_, info, name):
    global last_class_id
    last_class_id += 1
    new_class = {'id': last_class_id, 'name': name, "students": []}
    classes.append(new_class)
    return new_class


def all_students(_, info):
    return students


def all_classes(_, info):
    return classes


def add_student_to_class(_, info, class_id, student_id):
    student_data = None

    for student in students:
        if student['id'] == student_id:
            student_data = student

    for classs in classes:
        if classs['id'] == class_id:
            classs['students'].append(student_data)

    return classs