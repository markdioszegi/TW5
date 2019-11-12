import ui
import data_manager


def main():
    while True:
        show_menu()


def show_menu():
    students = data_manager.import_data()

    ui.print_menu(["Show students", "Create student", "Read student", "Exit program"])

    choices = ui.get_inputs([""], "Choose an option: ")

    for choice in choices:
        if choice == "1":
            ui.print_students(students)
        elif choice == "2":
            pass
        elif choice == "0":
            exit()
    

if __name__ == "__main__":
    main()