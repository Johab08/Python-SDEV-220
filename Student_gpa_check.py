# Name: Johabi Calas
# File Name: student_gpa_check.py
# Description: This app accepts student names and GPAs, checks if they qualify for 
#              the Dean's List (GPA >= 3.5) or the Honor Roll (GPA >= 3.25), and displays 
#              the appropriate message. The program stops when the last name 'ZZZ' is entered.

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        print("Exiting program.")
        break

    first_name = input("Enter the student's first name: ")

    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        continue

    print(f"\nStudent: {first_name} {last_name}")
    if gpa >= 3.5:
        print("Congratulations! You have made the Dean's List.")
    elif gpa >= 3.25:
        print("Congratulations! You have made the Honor Roll.")
    else:
        print("Keep working hard! You're not on the Dean's List or Honor Roll yet.")

