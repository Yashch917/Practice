#Write a program to accept a string from the user and check if it is a pangram (contains all alphabets from a–z).
str = input("Enter a string: ").lower()
alphabet = set('abcdefghijklmnopqrstuvwxyz')
if alphabet.issubset(set(str)):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")   