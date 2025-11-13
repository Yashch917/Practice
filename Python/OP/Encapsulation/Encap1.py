#Encapsulation is the process of binding data(Variables , Methods and Functions) and restricting access to some of the object's components.
# This is done to prevent the accidental modification of data.
#example: u have a bag but u dont want anyone to open it and see whats inside it.

#exapmle without Encapsulation
#student class with constructor(name and marks) self parameter and object creation
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Student Name:",self.name,", Marks:",self.marks)

s1=Student("Sakar",85)
s1=Student("Sakar",90)

