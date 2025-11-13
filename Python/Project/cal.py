#Make a simple Calculator Which peform operations like +,-,*,/

n1=eval(input("Enter First Number: "))
op=(input("Enter Operator: "))
n2=eval(input("Enter Second Number: "))

if op=='+':
    print("Addition: ",n1 ,op,n2,"=",n1+n2)
elif op=='-':
    print("Subtract: ",n1 ,op,n2,"=",n1-n2)
elif op=='*':
    print("Multiply: ",n1 ,op,n2,"=",n1*n2)
elif op=='/':
    print("Divide: ",n1 ,op,n2,"=",n1/n2)
else:
    print("Invalid Operation")