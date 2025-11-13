#class is like a blueprint for creating objects. It defines a set of attributes(data) and methods(functions) that the created objects will have.

class DemoClass: #class initialization
    x = 5#attribute
    
    def sum(self):#self is a reference to the current instance of the class
        a=int(input("Enter a number: "))#attribute
        print(a+40)
    def sub(self):
        a=int(input("Enter a number: "))#attribute
        print(a-20)

h1=DemoClass() #object creation
hr=DemoClass() #object creation
print("First Object: ", h1.x) #accessing attribute
print("Second Object: ", hr.x) #accessing attribute
h1.sum() #calling method
hr.sub() #calling method