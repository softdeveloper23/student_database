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

def add_course(students: dict, name: str, course: tuple) -> None:
    if name in students:
        # Initialize empty list if no courses yet
        if students[name] == "no completed courses":
            students[name] = []
            
        course_name, grade = course
        
        # Ignore courses with grade 0
        if grade == 0:
            return
            
        # Check if course already exists
        for i, (existing_course, existing_grade) in enumerate(students[name]):
            if existing_course == course_name:
                # Only update if new grade is higher
                if grade > existing_grade:
                    students[name][i] = (course_name, grade)
                return
                
        # If we get here, course doesn't exist yet, so add it
        students[name].append(course)

def summary(students: dict) -> None:
    # Print total number of students
    student_count = len(students)
    print(f"students {student_count}")
    
    # Variables to track most courses and best grade
    most_courses_count = 0
    most_courses_student = ""
    best_average = 0
    best_average_student = ""
    
    # Examine each student
    for name, courses in students.items():
        # Skip students with no courses
        if courses == "no completed courses":
            continue
            
        # Count courses for this student
        course_count = len(courses)
        if course_count > most_courses_count:
            most_courses_count = course_count
            most_courses_student = name
            
        # Calculate average grade
        total_grade = sum(grade for _, grade in courses)
        average = total_grade / course_count
        if average > best_average:
            best_average = average
            best_average_student = name
    
    # Print the results
    if most_courses_student:
        print(f"most courses completed {most_courses_count} {most_courses_student}")
    if best_average_student:
        print(f"best average grade {best_average:.1f} {best_average_student}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)