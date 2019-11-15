import ui

from student import student
from company import company
from position import position
from application import application


def main():
    while True:
        ui.print_menu("Main menu", ["Student module", "Company module", "Position module", "Application module", "Exit program"])

        choices = ui.get_inputs([""], "Choose an option: ")

        for choice in choices:
            if choice == "1":
                student.start_module()
            elif choice == "2":
                company.start_module()
            elif choice == "3":
                position.start_module()
            elif choice == "4":
                application.start_module()
            elif choice == "0":
                exit()
            """ else:
                raise KeyError("There is no such option!") """


if __name__ == "__main__":
    main()