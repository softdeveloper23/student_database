import student_database as db
import sys
from io import StringIO

# Function to capture print output
def capture_output(func, *args):
    original_stdout = sys.stdout
    output = StringIO()
    sys.stdout = output
    func(*args)
    sys.stdout = original_stdout
    return output.getvalue().strip()

# Test 1: Adding students
print("\n=== Test 1: Adding students ===")
students = {}
db.add_student(students, "Alice")
db.add_student(students, "Bob")
print(f"Students in database: {list(students.keys())}")
print(f"Expected: ['Alice', 'Bob']")

# Test 2: Basic course addition
print("\n=== Test 2: Basic course addition ===")
students = {}
db.add_student(students, "Charlie")
db.add_course(students, "Charlie", ("Python 101", 4))
output = capture_output(db.print_student, students, "Charlie")
print(output)
print("Expected output should show Charlie with 1 course (Python 101) with grade 4")

# Test 3: Ignoring zero grade courses
print("\n=== Test 3: Ignoring zero grade courses ===")
students = {}
db.add_student(students, "David")
db.add_course(students, "David", ("Database Design", 0))
output = capture_output(db.print_student, students, "David")
print(output)
print("Expected: David should have no courses")

# Test 4: Keeping the highest grade on repeat courses
print("\n=== Test 4: Keeping highest grade on repeat courses ===")
students = {}
db.add_student(students, "Eva")
db.add_course(students, "Eva", ("Algorithms", 3))
db.add_course(students, "Eva", ("Algorithms", 5))  # Higher grade should replace
db.add_course(students, "Eva", ("Algorithms", 2))  # Lower grade should be ignored
output = capture_output(db.print_student, students, "Eva")
print(output)
print("Expected: Eva should have Algorithms with grade 5")

# Test 5: Complex scenario for summary
print("\n=== Test 5: Complex summary test ===")
students = {}
db.add_student(students, "Frank")
db.add_student(students, "Grace")
db.add_student(students, "Hannah")

# Frank has many courses but low grades
db.add_course(students, "Frank", ("Course A", 1))
db.add_course(students, "Frank", ("Course B", 2))
db.add_course(students, "Frank", ("Course C", 1))
db.add_course(students, "Frank", ("Course D", 2))

# Grace has fewer courses but perfect grades
db.add_course(students, "Grace", ("Course X", 5))
db.add_course(students, "Grace", ("Course Y", 5))

# Hannah has no courses
output = capture_output(db.summary, students)
print(output)
print("Expected: 3 students, Frank has most courses (4), Grace has best average (5.0)")

# Test 6: Student not in database
print("\n=== Test 6: Student not in database ===")
students = {}
db.add_student(students, "Ian")
output = capture_output(db.print_student, students, "Unknown")
print(output)
print("Expected: 'Unknown: no such person in the database'") 