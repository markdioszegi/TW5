import ui
import data_manager
import common


class Student():
    def __init__(self, ID, name, age, status):
        self.ID = ID
        self.name = name
        self.age = age
        self.status = status

    def get_vars(self):
        return [self.ID, self.name, self.age, self.status]


def student_module():
    students = []

    for student in data_manager.import_data():
        students.append(Student(*student))

    back = False

    while not back:
        back = show_menu(students)


def show_menu(students):
    ui.print_menu("Student module", ["Show students", "Create a student", "Read a student",
                                     "Update a student", "Change a student's status", "Delete a student", "Return to main menu"])

    choices = ui.get_inputs([""], "Choose an option: ")

    for choice in choices:
        if choice == "1":
            show(students)
        elif choice == "2":
            create(students)
            data_manager.export_data(students)
        elif choice == "3":
            read(students)
        elif choice == "4":
            update(students)
            data_manager.export_data(students)
        elif choice == "5":
            change_status(students)
            data_manager.export_data(students)
        elif choice == "6":
            delete(students)
            data_manager.export_data(students)
        elif choice == "0":
            return True


def show(students):
    ui.print_table(students, ["ID", "Name", "Age", "Status"])


def create(students):
    inputs = ui.get_inputs(
        ["Name: ", "Age: ", "Status (1 - activated, 0 - deactivated): "])

    students.append(Student(common.generate_id(students), *inputs))


def read(students):
    student = common.check_id(students)
    if student:
        ui.print_table([student])
    else:
        ui.print_notification("No students with that ID!")


def update(students):
    student = common.check_id(students)
    if student:
        inputs = ui.get_inputs(["Name: ", "Age: "])
        (student.name, student.age) = (inputs[0], inputs[1])
    else:
        ui.print_notification("No students with that ID!")


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
        ui.print_notification("No students with that ID!")


def delete(students, id_=0):
    student = common.check_id(students)
    if student:
        students.remove(student)
    else:
        ui.print_notification("No students with that ID!")
