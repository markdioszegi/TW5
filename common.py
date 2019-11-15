import random
import ui


def generate_id(students):
    """
    numbers ascii: 48-57
    letters ascii: 65-90 
    """
    accepted = False

    while not accepted:
        symbols = "ĐßŁ&@"
        id_ = ""

        for i in range(2):
            id_ += chr(random.randrange(48, 57))
            id_ += chr(random.randrange(65, 90))
            id_ += chr(random.randrange(65, 90)).lower()
            id_ += list(symbols)[random.randrange(0, len(symbols))]

        id_ = "".join(random.sample(id_, len(id_)))

        for student in students:  # check if an id already exists
            if student.ID != id_:
                accepted = True

    return id_


def check_id(table):
    inputs = ui.get_inputs(["Enter the ID: "], "")

    for row in table:
        if inputs[0] == row.ID:
            return row


def check_company_name(companies, name):
    for company in companies:
        if company.name == name:
            return False
    
    return True