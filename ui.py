import os


OFFSET = 4


def print_menu(description, options):
    print(description)
    for i, option in enumerate(options):
        if i == len(options) - 1:
            print(" " * OFFSET + "{}. {}".format("0", option)) 
        else:
            print(" " * OFFSET + "{}. {}".format(i + 1, option))


def print_notification(err):
    print(" " * OFFSET + err)


def print_table(table, titles="", taken_seats=[""]):
    min_offset = 0

    for title in titles:
        if len(title) > min_offset:
            min_offset = len(title)

    ele_offsets = table[0].get_vars()

    for i, row in enumerate(table):
        if row.__class__.__name__ == "Position":
            for key in row.__dict__.keys():
                if key == "seats":
                    row.seats = row.seats + "/{}".format(taken_seats[i])
                        

    for row in table:
        for i, ele in enumerate(row.get_vars()):
            if len(str(ele)) > len(str(ele_offsets[i])):
                ele_offsets[i] = ele

    

    #print(ele_offsets)

    for i, title in enumerate(titles):
        print("-" * (len(ele_offsets[i]) + min_offset), end="")  #dashes above titles
    print()

    for i, title in enumerate(titles):
        print("{:^{}}".format(title, len(ele_offsets[i]) + min_offset), end="")   #titles
    print()
    
    for i, title in enumerate(titles):
        print("-" * (len(ele_offsets[i]) + min_offset), end="")  #dashes below titles
    print()

    for row in table:
        for i, ele in enumerate(row.get_vars()):
            print("{:^{}}".format(ele, len(ele_offsets[i]) + min_offset), end="")
        print()

    for i, title in enumerate(titles):
        print("-" * (len(ele_offsets[i]) + min_offset), end="")  #dashes below data
    print()
    
    """ print(" | ".join(titles))

    for row in table:
        print(", ".join(row.get_vars())) """


def print_student(student, positions, companies):
    if positions and companies: 
        print(student.name + "'s applications: ")

        for position, company in zip(positions, companies):
            print(" " * OFFSET + position + " at " + company)
    else:
        print(student.name + " does not have any applications!")


def print_company(company, positions):
    if positions:
        print(company.name + "'s positions: ")

        for position in positions:
            print(" " * OFFSET + position.description)
    else:
        print(company.name + " does not have any positions.")


def print_position(position, students):
    if students:
        print(position.description + " applications: ")

        for student in students:
            print(" " * OFFSET + student.name)
    else:
        print(position.description + " does not have any students.")


def get_inputs(inputs, description="Fill the blanks"):
    inputs_ = []

    print(description)

    for input_ in inputs:
        inputs_.append(input(" " * OFFSET + input_))

    return inputs_
