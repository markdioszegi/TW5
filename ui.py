def print_menu(options):
    print("Main Menu")
    for i, option in enumerate(options):
        if i == len(options) - 1:
            print(" " * 4 + "{}. {}".format("0", option)) 
        else:
            print(" " * 4 + "{}. {}".format(i + 1, option)) 


def print_students(students):
    for student in students:
        print(student)


def get_inputs(inputs, description="Fill the blanks"):
    inputs_ = []

    print(description)

    for input_ in inputs:
        inputs_.append(input(" " * 4 + input_))

    return inputs_
