import json
import re
from pathlib import Path


# ---------------------------------------------------------
# STUDENT RECORD MANAGER
# ---------------------------------------------------------

# File where student records will be stored
FILE_NAME = "students.json"


# ---------------------------------------------------------
# CUSTOM EXCEPTION
# ---------------------------------------------------------

class InvalidEmailError(Exception):
    """
    Custom exception used when an invalid email address
    is entered by the user.
    """
    pass


# ---------------------------------------------------------
# EMAIL VALIDATION USING REGEX
# ---------------------------------------------------------

def validate_email(email):
    """
    Validates the email address using Regular Expression.

    Example of valid emails:
        student@gmail.com
        abc123@yahoo.com

    Example of invalid emails:
        student@
        @gmail.com
        student@gmail
    """

    # Regular expression pattern for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Check whether email matches the pattern
    if re.match(pattern, email):
        return True

    # If email does not match, raise custom exception
    raise InvalidEmailError("Invalid email address!")


# ---------------------------------------------------------
# LOAD STUDENTS FROM FILE
# ---------------------------------------------------------

def load_students():
    """
    Reads student records from students.json.

    Returns:
        List of students
    """

    try:
        # Check whether the file exists
        if not Path(FILE_NAME).exists():
            return []

        # Open file in read mode
        with open(FILE_NAME, "r") as file:

            # Read JSON data
            students = json.load(file)

            return students

    except json.JSONDecodeError:
        print("Error: Student file contains invalid data.")
        return []

    except PermissionError:
        print("Error: Permission denied while reading the file.")
        return []

    except Exception as error:
        print("Unexpected error:", error)
        return []


# ---------------------------------------------------------
# SAVE STUDENTS TO FILE
# ---------------------------------------------------------

def save_students(students):
    """
    Saves all student records into students.json.
    """

    try:
        # Open file in write mode
        with open(FILE_NAME, "w") as file:

            # Convert Python list into JSON format
            json.dump(students, file, indent=4)

        print("\nStudent data saved successfully!")

    except PermissionError:
        print("Error: Permission denied while saving the file.")

    except Exception as error:
        print("Unexpected error:", error)


# ---------------------------------------------------------
# ADD STUDENT
# ---------------------------------------------------------

def add_student():
    """
    Adds a new student record.
    """

    print("\n================================")
    print("         ADD STUDENT")
    print("================================")

    try:
        # Get Student ID
        student_id = input("Enter Student ID: ").strip()

        # Check empty Student ID
        if student_id == "":
            raise ValueError("Student ID cannot be empty.")

        # Load existing students
        students = load_students()

        # Check whether Student ID already exists
        for student in students:
            if student["student_id"] == student_id:
                raise ValueError("Student ID already exists.")

        # Get student name
        name = input("Enter Full Name: ").strip()

        if name == "":
            raise ValueError("Name cannot be empty.")

        # Get email
        email = input("Enter Email: ").strip()

        # Validate email using Regex
        validate_email(email)

        # Get age
        age_input = input("Enter Age: ").strip()

        # Convert age into integer
        age = int(age_input)

        # Validate age
        if age <= 0 or age > 100:
            raise ValueError("Age must be between 1 and 100.")

        # Create student dictionary
        student = {
            "student_id": student_id,
            "name": name,
            "email": email,
            "age": age
        }

        # Add student to list
        students.append(student)

        # Save updated list
        save_students(students)

        print("\nStudent added successfully!")

    except InvalidEmailError as error:
        print("Email Error:", error)

    except ValueError as error:
        print("Input Error:", error)

    except Exception as error:
        print("Unexpected Error:", error)


# ---------------------------------------------------------
# READ STUDENT DATA
# ---------------------------------------------------------

def read_students():
    """
    Displays all student records stored in the JSON file.
    """

    print("\n================================")
    print("       STUDENT RECORDS")
    print("================================")

    students = load_students()

    # Check if there are no records
    if len(students) == 0:
        print("No student records found.")
        return

    # Display each student
    for number, student in enumerate(students, start=1):

        print("\nStudent", number)
        print("----------------------------")
        print("Student ID :", student["student_id"])
        print("Name       :", student["name"])
        print("Email      :", student["email"])
        print("Age        :", student["age"])


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main():
    """
    Displays the main menu and controls the program.
    """

    while True:

        print("\n================================")
        print("     STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":
                add_student()

            elif choice == "2":
                read_students()

            elif choice == "3":
                print("\nThank you for using Student Record Manager!")
                break

            else:
                raise ValueError(
                    "Invalid choice. Please select 1, 2, or 3."
                )

        except ValueError as error:
            print("Error:", error)

        except Exception as error:
            print("Unexpected Error:", error)


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
