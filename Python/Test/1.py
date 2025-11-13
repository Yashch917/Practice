#Write a Python program to check the datatype of each element in the list: [10, 12.5, "AI", True].
l=[10, 12.5, "AI", True]
print(l)
n=input("Enter the index to check datatype: ")
print(type(l[int(n)]))