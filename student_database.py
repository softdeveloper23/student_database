def add_student(students : dict, name : str) -> None:
    students[name] = "no completed courses"

def print_student(students : dict, name : str) -> None:
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        
        if students[name] == "no completed courses":
            print(f" {students[name]}")
        else:
            courses = students[name]
            print(f" {len(courses)} completed courses:")

            total_grade = 0
            for course_name, grade in courses:
                print(f"  {course_name} {grade}")
                total_grade += grade

            average = total_grade / len(courses) if courses else 0
            print(f" average grade {average:.1f}")

def add_course(students: dict, name : str, course: tuple) -> None:
    if name in students:
        if students[name] == "no completed courses":
            students[name] = []
        if course[1] != 0:
            students[name].append(course)

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")