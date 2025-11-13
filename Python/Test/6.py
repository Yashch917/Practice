#Write a program that prints all numbers from 1 to 50 that are divisible by both 3 and 5.

for i in range(1,51):
    if i%3==0 and i%5==0:
        print(i)