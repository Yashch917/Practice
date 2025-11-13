#Write a program to create a set of numbers from 1 to 10 and remove even numbers from it.
my_set = set(range(1, 11))
my_set = {num for num in my_set if num % 2 != 0}
print("The set after removing even numbers is:", my_set)