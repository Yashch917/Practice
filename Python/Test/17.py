#Write a program to count the frequency of each character in a string using a dictionary.
str=input("Enter a string: ")
freq={}
for char in str:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print("Character frequency is:", freq)