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


def print_table(table, titles=""):
    print("|".join(titles))

    for row in table:
        print(", ".join(row.get_vars()))


def get_inputs(inputs, description="Fill the blanks"):
    inputs_ = []

    print(description)

    for input_ in inputs:
        inputs_.append(input(" " * OFFSET + input_))

    return inputs_
