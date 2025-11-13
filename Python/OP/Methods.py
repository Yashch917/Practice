#function is a block of code that performs a specific task
#it is defined outside a class(independent)
#it is used to describe a behavior of an object
#it is always using an object

class robot:
    a='hello'
    def speak(self):#self is a reference to the current instance of the class
        input_text=input("Enter a name:")
        print("Robot says: ",self.a, input_text)

r1=robot() #object creation
r1.speak() #calling method


#create class robot1 10 20 show method self.a create another showvalue created self attribute and print hello welcome sakar robotics
#method value and use self,a,b print addition is a+b and create object to call all methods and print

class robot1:
    a=10

    def show(self):
        print(self.a)
    def ShowValue(self):
        print("Hello, Welcome to Sakar Robotics.")
    def Value(self,a,b):
        print("Addition is:", a+b)

r2=robot1()
r2.show()
r2.ShowValue()
r2.Value(20,30)
    
class car:
    def mercedes(self):
        print("MERCEDES COMPANY")
    
car1=car()
car1.mercedes()
