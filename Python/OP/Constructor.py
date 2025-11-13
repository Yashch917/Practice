#A constructor is a special method that is automatically called when an object of a class is created.
# It is used to initialize the attributes of the object.
# In Python, the constructor method is defined using the __init__() method.

class Robo:
    def __init__(self,Name):
        print("Welcome to Constructor",Name)
        self.Name=Name

    def Sakar(self):
        print("Hello, Watashiwa ",self.Name)

r1=Robo("Sakar")
r2=Robo("Swaroop")
r2.Sakar()
r1.Sakar()


