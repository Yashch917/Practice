# Write a program to find the maximum and minimum element from a list.
my_list = input("Enter a list of numbers separated by spaces: ").split()
my_list = [int(i) for i in my_list]
max_element = max(my_list)
min_element = min(my_list)
print("The maximum element in the list is:", max_element)
print("The minimum element in the list is:", min_element)