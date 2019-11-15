def import_data(filename):
    lines = []

    with open(filename, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            lines.append(line[:-1].split(","))
    
    return lines

def export_data(students, filename):
    with open(filename, "w", encoding="UTF-8") as f:
        for student in students:
            f.write(",".join(student.get_vars()) + "\n")