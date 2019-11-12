def import_data(filename="students.csv"):
    lines = []
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            lines.append(line[:-1].split(","))
    
    return lines

def export_data():
    pass