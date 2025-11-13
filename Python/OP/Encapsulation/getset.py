#encapsulation with getters and setters
#getter to get the value of a private attribute
#setter to set,change the value of a private attribute
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
        print("Student Name:",self.name,", Marks:",self.__marks)
    def Name(self):
        return self.name
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if 0<= marks <=100:
           self.__marks=marks
        else:
            print("Invalid marks")
s1=Student("Sir",85)
print(s1.get_marks())
s1.set_marks(95)
print(s1.get_marks())
s1.set_marks(105)
print(s1.get_marks())   