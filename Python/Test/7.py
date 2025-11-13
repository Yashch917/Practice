#Write a program to find the factorial of a number using a while loop.
n=int(input("Enter the number to find factorial: "))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1   
print("Factorial of",n,"is",fact)