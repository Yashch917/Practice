#create a python file that allows user to add student details (name, roll no, course) save details in the txt file student.txt
#option to view all students

def add_student():
    with open('student.txt','a') as file:
        try:
            name=input("Enter student name: ")
            roll_no=int(input("Enter roll number: "))
            course=input("Enter course: ")
            file.write(f"Name: {name}, Roll No: {roll_no}, Course: {course}\n")
            print("Student details added successfully.\n2")
        except Exception as e:
            print(f"Invalid Input.{e}")
            print("Failed to add student details.Try Again\n")


def view_students():
    try:
        with open('student.txt','r') as file:
            content=file.read()
            print("Student Details:")
            print(content)
    except Exception as e:
        print(f"An error occurred: {e}")


while True:
    print("1. Add Student")
    print("2. View All Students")
    choice=input("Enter your choice (1 or 2): ")
    if choice=='1':
        add_student()
    elif choice=='2':
        view_students()
    else:
        print("Invalid choice. Please enter 1 or 2.")