#Write a program to take two numbers from the user and print the larger one using conditional operators.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    print(a,"is larger")
elif b>a:
    print(b,"is larger")
else:
    print("Both are equal")