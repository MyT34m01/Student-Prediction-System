import random
import re

# Data structure to store student information
students = {}

# Predefined subjects for each semester
first_semester_subjects = [
    'SSP', 'LWR', 'PSE', 'CET', 'PROG1L', 'ITC', 'DMATH', 'PATHFIT1', 'NSTP1'
]
second_semester_subjects = [
    'CPH', 'CMW', 'CUS', 'PROG2L', 'DSAAL', 'SIPP', 'NSTP2', 'PATHFIT2'
]

# Updated course descriptions and units
course_descriptions = {
    'SSP': 'Religious Experiences and Spirituality',
    'LWR': 'Life and Works of Rizal',
    'PSE': 'Peace Studies Education',
    'CET': 'Ethics',
    'PROG1L': 'Fundamentals of Programming',
    'ITC': 'Introductions to Computing',
    'DMATH': 'Discrete Mathematics',
    'PATHFIT1': 'Physical Activities Toward Health and Fitness 1: Movement Enhancement',
    'NSTP1': 'Civic Welfare Training Service 1',
    'CPH': 'Readings in Philippine History',
    'CMW': 'Mathematics in the Modern World',
    'CUS': 'Understanding the Self',
    'PROG2L': 'Intermediate Programming',
    'DSAAL': 'Data Structures and Algorithms',
    'SIPP': 'Social Issues and Professional Practice',
    'NSTP2': 'Civic Welfare Training Service 2',
    'PATHFIT2': 'Physical Activities Toward Health and Fitness 2: Physical Fitness & Aerobics'
}
course_units = {
    'SSP': 3, 'LWR': 3, 'PSE': 3, 'CET': 3, 'PROG1L': 3, 'ITC': 3,
    'DMATH': 3, 'PATHFIT1': 2, 'NSTP1': 3, 'CPH': 3, 'CMW': 3, 'CUS': 3,
    'PROG2L': 3, 'DSAAL': 3, 'SIPP': 3, 'NSTP2': 3, 'PATHFIT2': 2
}

# Function to generate a random 8-digit student ID
def generate_student_id():
    while True:
        student_id = f"{random.randint(10000000, 99999999)}"
        if student_id not in students:
            return student_id

# Function to validate email format
def validate_email(email):
    # Regular expression pattern for a valid email
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    # Return True if the email matches the pattern, otherwise False
    return email_regex.match(email) is not None

# Function to input student details and grades
def input_student_data():
    last_name = input("Enter student's last name: ")
    first_name = input("Enter student's first name: ")
    middle_name = input("Enter student's middle name (leave blank if not applicable): ")
    gender = input("Enter student's gender (M/F): ").upper()
    while gender not in ['M', 'F']:
        print("Invalid input. Please enter 'M' for male or 'F' for female.")
        gender = input("Enter student's gender (M/F): ").upper()
    
    address = input("Enter student's address: ")
    shs_strand = input("Enter student's SHS Strand: ")
    honors = input("Enter student's honors (if any): ")
    
    email = input("Enter student's email address: ")
    while not validate_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter student's email address: ")

    print("Enter grades for the first semester:")
    first_semester_grades = {}
    for subject in first_semester_subjects:
        while True:
            try:
                grade = float(input(f"Enter grade for {subject} ({course_descriptions[subject]}, {course_units[subject]} units) (50-100): "))
                if 50 <= grade <= 100:
                    first_semester_grades[subject] = grade
                    break
                else:
                    print("Grade must be between 50 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
    
    print("Enter grades for the second semester:")
    second_semester_grades = {}
    for subject in second_semester_subjects:
        while True:
            try:
                grade = float(input(f"Enter grade for {subject} ({course_descriptions[subject]}, {course_units[subject]} units) (50-100): "))
                if 50 <= grade <= 100:
                    second_semester_grades[subject] = grade
                    break
                else:
                    print("Grade must be between 50 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
    
    student_id = generate_student_id()  # Generate a unique student ID
    students[student_id] = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'gender': gender,
        'address': address,
        'shs_strand': shs_strand,
        'honors': honors,
        'email': email,
        'first_semester_grades': first_semester_grades,
        'second_semester_grades': second_semester_grades
    }
    print(f"Student added successfully with Student ID: {student_id}.")

# Function to determine pass/fail status
def get_status(grade):
    return "Passed" if grade >= 75 else "Failed"

# Function to list all students and their grades
def list_students():
    if not students:
        print("No students available.")
        return
    
    for student_id, info in students.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {info['last_name']}, {info['first_name']} {info['middle_name']}")
        print(f"Gender: {'Male' if info['gender'] == 'M' else 'Female'}")
        print(f"Address: {info['address']}")
        print(f"SHS Strand: {info['shs_strand']}")
        print(f"Honors: {info['honors']}")
        print(f"Email: {info['email']}")
        
        print("First Semester Grades:")
        for subject in first_semester_subjects:
            grade = info['first_semester_grades'].get(subject, 'N/A')
            status = get_status(grade) if grade != 'N/A' else 'N/A'
            print(f"  {subject}: {grade} ({course_descriptions[subject]}, {course_units[subject]} units) - {status}")
        
        print("Second Semester Grades:")
        for subject in second_semester_subjects:
            grade = info['second_semester_grades'].get(subject, 'N/A')
            status = get_status(grade) if grade != 'N/A' else 'N/A'
            print(f"  {subject}: {grade} ({course_descriptions[subject]}, {course_units[subject]} units) - {status}")
        
        print("-" * 40)

# Main function to handle input and display
if __name__ == "__main__":
    while True:
        print("1. Add student")
        print("2. List students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_student_data()
        elif choice == '2':
            list_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
