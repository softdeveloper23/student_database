def add_student(students : dict, name : str) -> None:
    students[name] = "no completed courses"

def print_student(students : dict, name : str) -> None:
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        print(f"\t{students[name]}")
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")