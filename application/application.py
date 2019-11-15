import ui
import data_manager
import common

from student import student
from position import position


class Application():
    def __init__(self, ID, status, student_id, position_id):
        self.ID = ID
        self.status = status
        self.student_id = student_id
        self.position_id = position_id

    def get_vars(self):
        return [self.ID, self.status, self.student_id, self.position_id]


def load():
    applications = []

    for application in data_manager.import_data("application/applications.csv"):
        applications.append(Application(*application))

    return applications


def start_module():
    back = False

    while not back:
        back = show_menu(load())


def show_menu(applications):
    ui.print_menu("Applications module", ["Show applications", "Create an application",
                                          "Update an application", "Delete an application", "Return to main menu"])

    choices = ui.get_inputs([""], "Choose an option: ")

    for choice in choices:
        if choice == "1":
            show(applications)
        elif choice == "2":
            create(applications)
            data_manager.export_data(applications, "application/applications.csv")
        elif choice == "3":
            update(applications)
            data_manager.export_data(applications, "application/applications.csv")
        elif choice == "4":
            delete(applications)    #TODO
        elif choice == "0":
            return True


def show(applications):
    ui.print_table(applications, ["ID", "Status", "Student ID", "Position ID"])


def create(applications):
    inputs = ui.get_inputs(
        ["Status: ", "Student ID: ", "Position ID: "])

    allowed = True

    try:
        if int(inputs[0]) > 1 or int(inputs[0]) < 0:
            ui.print_notification("Status could be only either 1 or 0!")
            allowed = False
    except ValueError:
        ui.print_notification("Only numbers are allowed!")

    if inputs[1] not in student.get_students_id():
        ui.print_notification("Wrong student ID!")
        allowed = False

    if inputs[2] not in position.get_positions_id():
        ui.print_notification("Wrong position ID!")
        allowed = False

    for application in applications:
        if inputs[2] == application.position_id and inputs[1] == application.student_id:
            ui.print_notification("Student already applied to this position!")
            allowed = False
            #break

    if inputs[0] == "1":    #check if the user can create an application and not exceeded the available seats
        taken_seats = position.get_taken_seats()[0]
        max_seats = position.get_taken_seats()[1]

        for i in range(len(max_seats)):
            if max_seats[i].ID == inputs[2]:
                if taken_seats[i] >= int(max_seats[i].seats):
                    ui.print_notification("Position is full!")
                    allowed = False

    if allowed:
        applications.append(Application(common.generate_id(applications), *inputs))
        ui.print_notification("Application added!")


def update(applications):
    application = common.check_id(applications)
    if application:
        inputs = ui.get_inputs(["Status"])

        taken_seats = position.get_taken_seats()[0]
        max_seats = position.get_taken_seats()[1]

        for i in range(len(max_seats)):
            if max_seats[i].ID == application.position_id:
                if inputs[0] == "1":
                    if taken_seats[i] >= int(max_seats[i].seats):
                        ui.print_notification("Status can't be changed! Seats are already full!")
                else:
                    application.status = inputs[0]
                    ui.print_notification("Status successfully changed.")
    else:
        ui.print_notification("No application found with that ID!")


def get_applications_by_student_id(student_id):
    applications = load()
    apps = []

    for application in applications:
        if application.student_id == student_id:
            apps.append(application)

    return apps


def get_applications_by_position_id(position_id):
    applications = load()
    apps = []

    for application in applications:
        if application.position_id == position_id:
            apps.append(application)

    return apps