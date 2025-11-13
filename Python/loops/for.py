# Looping means repeating a block of code multiple times 
# until a condition is false or until items are finished.
# Python has two main types of loops:
# for loop & while loop 

# range() in Python
# ---> The range() function generates a sequence of numbers. 
# It does not store all numbers at once but creates them on demand.
# ✅ Syntax = range(start, stop, step)

for i in range(5):   # starts from 0 and stop at stop-1
    print(i)
    
# 2) range(start, stop)

for i in range(2, 6):   # Starts at 2 and goes till 5
    print(i)

# 3) range(start, stop, step)

for i in range(1, 10, 2):   # Numbers jump by 2 (step).
    print(i)

print("Multiplication Table of 2")

for i in range(1,11):
    print("2 *",i,"=",2*i)