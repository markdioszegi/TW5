import ui
import data_manager
import common

from position import position


class Company():
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name


    def get_vars(self):
        return [self.ID, self.name]


def load():
    companies = []

    for company in data_manager.import_data("company/companies.csv"):
        companies.append(Company(*company))

    return companies


def start_module():
    back = False

    while not back:
        back = show_menu(load())


def show_menu(companies):
    ui.print_menu("Companies module", ["Show companies", "Create a company", "Read a company",
                                       "Update a company", "Delete a company", "Return to main menu"])

    choices = ui.get_inputs([""], "Choose an option: ")

    for choice in choices:
        if choice == "1":
            show(companies)
        elif choice == "2":
            create(companies)
            data_manager.export_data(companies, "company/companies.csv")
        elif choice == "3":
            read(companies)
        elif choice == "4":
            update(companies)
            data_manager.export_data(companies, "company/companies.csv")
        elif choice == "5":
            delete(companies)
            data_manager.export_data(companies, "company/companies.csv")
        elif choice == "0":
            return True


def show(companies):
    ui.print_table(companies, ["ID", "Name"])


def create(companies):
    inputs = ui.get_inputs(["Name: "])

    if common.check_company_name(companies, inputs[0]):
        companies.append(Company(common.generate_id(companies), *inputs))
        ui.print_notification("Company added!")
    else:
        ui.print_notification("Company name already exists!")


def read(companies):
    company = common.check_id(companies)
    if company:
        positions = position.get_positions(company)

        ui.print_company(company, positions)
    else:
        ui.print_notification("No company found with that ID!")


def update(companies):
    company = common.check_id(companies)
    if company:
        inputs = ui.get_inputs(["Name: "])
        if common.check_company_name(companies, inputs[0]):
            company.name = inputs[0]
        else:
            ui.print_notification("Cannot change company name to " + inputs[0] + " because it already exists!")
    else:
        ui.print_notification("No company found with that ID!")


def delete(companies):
    company = common.check_id(companies)
    if company:
        if not position.get_positions(company):
            companies.remove(company)
            ui.print_notification("Company " + company.name + " deleted.")
        else:
            ui.print_notification("This company has positions!")
    else:
        ui.print_notification("No company found with that ID!")


def get_company_ids():
    ids = []

    for company in load():
        ids.append(company.ID)

    return ids


def get_company_names(company_ids):
    companies = load()

    names = []

    for company_id in company_ids:
        for company in companies:
            if company.ID == company_id:
                names.append(company.name)

    return names