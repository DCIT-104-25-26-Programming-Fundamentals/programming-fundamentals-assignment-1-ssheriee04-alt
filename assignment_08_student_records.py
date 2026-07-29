# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#
def display_menu():
    """Displays the main menu options for the system."""
    print("========================================")
    print("        STUDENT RECORD SYSTEM MENU       ")
    print("========================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def add_student(students):
    """Prompts for student details and appends a new student dictionary to the list."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()
    
    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Number of scores must be at least 1.")
            return
        
        scores = []
        for i in range(1, num_scores + 1):
            score = float(input(f"Enter score {i}: "))
            if score.is_integer():
                score = int(score)
            scores.append(score)
            
        student_record = {
            "name": name,
            "id": student_id,
            "scores": scores
        }
        students.append(student_record)
        print(f'Student "{name}" added successfully.')
        
    except ValueError:
        print("Invalid input. Please enter valid numbers for scores.")

def calculate_student_average(scores):
    """Calculates and returns the average of a list of scores."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def display_all_students(students):
    """Displays all students in a neatly aligned table format."""
    if not students:
        print("No student records found.")
        return

    print("----------------------------------------------------------------")
    print(f"{'Name':<18} {'ID':<12} {'Scores':<18} {'Average':<8}")
    print("----------------------------------------------------------------")
    
    for s in students:
        avg = calculate_student_average(s["scores"])
        scores_str = ", ".join(str(x) for x in s["scores"])
        print(f"{s['name']:<18} {s['id']:<12} {scores_str:<18} {avg:.2f}")
        
    print("----------------------------------------------------------------")

def calculate_specific_average(students):
    """Searches for a student by ID and prints their calculated average."""
    target_id = input("Enter student ID: ").strip()
    
    for s in students:
        if s["id"] == target_id:
            avg = calculate_student_average(s["scores"])
            print(f"{s['name']}'s average score: {avg:.2f}")
            return
            
    print(f"Error: Student with ID '{target_id}' not found.")

def main():
    students = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            calculate_specific_average(students)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        print()  # Spacer line

if __name__ == "__main__":
    main()


