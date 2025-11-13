#Write a program to create a dictionary of 3 students with their names as keys and marks as values. Print only the names of students who scored more than 50 marks.
students = {'Alice': 45, 'Bob': 75, 'Charlie': 60}
for name, marks in students.items():
    if marks > 50:
        print(name) 