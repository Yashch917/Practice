#Write a program to count how many vowels are present in a string entered by the user.
s=input("Enter a string: ")
count=0
for i in s:
    if i in 'aeiouAEIOU':
        count=count+1
print("Number of vowels in the string is:",count)