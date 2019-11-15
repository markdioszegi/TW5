import ui
import data_manager
import common

from company import company
from application import application
from student import student

class Position():
    def __init__(self, ID, description, seats, company_id):
        self.ID = ID
        self.description = description
        self.seats = seats
        self.company_id = company_id


    def get_vars(self):
        return [self.ID, self.description, self.seats, self.company_id]


def load():
    positions = []

    for position in data_manager.import_data("position/positions.csv"):
        positions.append(Position(*position))

    return positions


def start_module():
    back = False

    while not back:
        back = show_menu(load())


def show_menu(positions):
    ui.print_menu("Position module", ["Show positions", "Create a position", "Read a position",
                                     "Update a position", "Delete a position", "Return to main menu"])

    choices = ui.get_inputs([""], "Choose an option: ")

    for choice in choices:
        if choice == "1":
            show(positions)
        elif choice == "2":
            create(positions)
            data_manager.export_data(positions, "position/positions.csv")
        elif choice == "3":
            read(positions)
        elif choice == "4":
            update(positions)
            data_manager.export_data(positions, "position/positions.csv")
        elif choice == "5":
            delete(positions)
            data_manager.export_data(positions, "position/positions.csv")
        elif choice == "0":
            return True


def show(positions):
    taken_seats = get_taken_seats()[0]

        #taken_seats[i] += len(students)

    ui.print_table(positions, ["ID", "Description", "Seats (Available/Taken)", "Company ID"], taken_seats)


def create(positions):
    inputs = ui.get_inputs(
        ["Description: ", "Seats: ", "Company ID: "])

    allowed = True

    if not inputs[0]:
        ui.print_notification("Descriptions cannot be empty!")
        allowed = False
        
    try:
        if int(inputs[1]) < 1:
            ui.print_notification("Seats must be greater than 0!")
            allowed = False
    except ValueError:
        ui.print_notification("Only numbers are allowed!")

    if inputs[2] not in company.get_company_ids():
        ui.print_notification("Wrong company ID!")
        allowed = False

    if allowed:
        positions.append(Position(common.generate_id(positions), *inputs))
        ui.print_notification("Position added!")


def read(positions):
    position = common.check_id(positions)
    if position:
        apps = application.get_applications_by_position_id(position.ID)
        students = student.get_students_from_applications(apps)

        ui.print_position(position, students)
    else:
        ui.print_notification("No position found with that ID!")


def update(positions):
    position = common.check_id(positions)
    if position:
        inputs = ui.get_inputs(["Description: "])
        position.description = inputs[0]
    else:
        ui.print_notification("No position found with that ID!")


def delete(positions, id_=0):
    position = common.check_id(positions)
    if position:
        if not application.get_applications_by_position_id(position.ID):
            positions.remove(position)
            ui.print_notification("Position " + position.description + " deleted.")
        else:
            ui.print_notification("This position has applications!")
    else:
        ui.print_notification("No position found with that ID!")


def get_positions(company):
    positions = load()
    positions_ = []

    for position in positions:
        if company.ID == position.company_id:
            positions_.append(position)

    return positions_


def get_positions_id():
    ids = []

    for position in load():
        ids.append(position.ID)

    return ids


def get_positions_description(apps):
    positions = load()

    descs = []

    for app in apps:
        for pos in positions:
            if app.position_id == pos.ID:
                descs.append(pos.description)

    return descs


def get_positions_id_by_applications(apps):
    ids = []

    for position in load():
        for app in apps:
            if app.position_id == position.ID:
                ids.append(position.company_id)

    return ids

def get_taken_seats():
    """
    Gives back a list with the taken seats corresponding to its position id.

    return list of lists: [[taken_seats], []]
    """
    positions = load()

    taken_seats = [0 for x in range(len(positions))]
    positions_ = []

    for i, position in enumerate(positions):
        apps = application.get_applications_by_position_id(position.ID)
        students = student.get_students_from_applications(apps)

        for app in apps:
            if app.status == "1":
                taken_seats[i] += 1

        positions_.append(position)
    
    return [taken_seats, positions_]