import ui
import data_manager
import common

from application import application
from position import position
from company import company


class Student():
    def __init__(self, ID, name, age, status):
        self.ID = ID
        self.name = name
        self.age = age
        self.status = status


    def get_vars(self):
        return [self.ID, self.name, self.age, self.status]


def load():
    students = []

    for student in data_manager.import_data("student/students.csv"):
        students.append(Student(*student))

    return students


def start_module():
    back = False

    while not back:
        back = show_menu(load())


def show_menu(students):
    ui.print_menu("Student module", ["Show students", "Create a student", "Read a student",
                                     "Update a student", "Change a student's status", "Delete a student", "Return to main menu"])

    choices = ui.get_inputs([""], "Choose an option: ")

    for choice in choices:
        if choice == "1":
            show(students)
        elif choice == "2":
            create(students)
            data_manager.export_data(students, "student/students.csv")
        elif choice == "3":
            read(students)
        elif choice == "4":
            update(students)
            data_manager.export_data(students, "student/students.csv")
        elif choice == "5":
            change_status(students)
            data_manager.export_data(students, "student/students.csv")
        elif choice == "6":
            delete(students)
            data_manager.export_data(students, "student/students.csv")
        elif choice == "0":
            return True


def show(students):
    ui.print_table(students, ["ID", "Name", "Age", "Status"])


def create(students):
    inputs = ui.get_inputs(
        ["Name: ", "Age: ", "Status (1 - activated, 0 - deactivated): "])

    allowed = True

    try:
        if int(inputs[1]) > 100 and int(inputs[1]) < 16:
            ui.print_notification("Wrong age! (16-99)")
            allowed = False
    except ValueError:
        ui.print_notification("Only numbers are allowed!")

    try:
        if int(inputs[2]) > 1 or int(inputs[2]) < 0:
            ui.print_notification("Status could be only either 1 or 0!")
            allowed = False
    except ValueError:
        ui.print_notification("Only numbers are allowed!")

    if allowed:
        ui.print_notification("Student added!")

    students.append(Student(common.generate_id(students), *inputs))


def read(students):
    student = common.check_id(students)
    if student:
        apps = application.get_applications_by_student_id(student.ID)
        position_descs = position.get_positions_description(apps)

        company_ids = position.get_positions_id_by_applications(apps)
        company_names = company.get_company_names(company_ids)

        ui.print_student(student, position_descs, company_names)
    else:
        ui.print_notification("No student found with that ID!")


def update(students):
    student = common.check_id(students)
    if student:
        inputs = ui.get_inputs(["Name: ", "Age: "])
        (student.name, student.age) = (inputs[0], inputs[1])
    else:
        ui.print_notification("No student found with that ID!")


def change_status(students):
    student = common.check_id(students)
    if student:
        if student.status == "1":
            student.status = "0"
            ui.print_notification("Status changed to: 0 (deactivated)")
        else:
            student.status = "1"
            ui.print_notification("Status changed to: 1 (activated)")
    else:
        ui.print_notification("No student found with that ID!")


def delete(students, id_=0):
    student = common.check_id(students)
    if student:
        if not application.get_applications_by_student_id(student.ID):
            students.remove(student)
            ui.print_notification(student.name + " deleted.")
        else:
            ui.print_notification("This student has applications!")
    else:
        ui.print_notification("No student found with that ID!")


def get_students_id():
    ids = []

    for student in load():
        ids.append(student.ID)

    return ids


def get_students_from_applications(apps):
    students = load()
    students_ = []

    for app in apps:
        for student in students:
            if app.student_id == student.ID:
                students_.append(student)

    return students_