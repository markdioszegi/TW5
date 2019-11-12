import ui
from student import student


def main():
    while True:
        ui.print_menu("Main menu", ["Student module", "Company module", "Position module", "Application module", "Exit program"])

        choices = ui.get_inputs([""], "Choose an option: ")

        for choice in choices:
            if choice == "1":
                student.student_module()
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "0":
                exit()
            """ else:
                raise KeyError("There is no such option.") """


if __name__ == "__main__":
    main()