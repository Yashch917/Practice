#Write a program to print the multiplication table of any number entered by the user (1 to 10).
n=int(input("Enter the number to print multiplication table: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)