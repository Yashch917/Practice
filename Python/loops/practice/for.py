#print number 1 to 10 using for loop
for i in range(1,11):
    print(i)

#reverse order
for i in range(10,0,-1):
    print(i)


#print even number 2 to 20
for i in range(2,21,2):
    print(i)

#print odd number 1 to 20
for i in range(1,20,2):
    print(i)

#print table of 9
for i in range(1,11):
    print("9 *",i,"=",9*i)


#Sum of first 20 natural number
total=0
for i in range(1,21):
    total+=i
print("Sum of 1 to 20 is:",total)

#factorial of 6
fact=1
for i in range(1,7):
    fact*=i
print("Factorial of 6 is:",fact)

#cube of first 5 natural number
for i in range(1,6):
    print(i,"** 3 =",i**3)

#print all the multiples of 4 between 1 to 40
for i in range(1,41):
    if i%4==0:
        print(i)

#Used to skip the current iteration of the loop and move to the next iteration.
for i in range(1,11):
    if i==5:
        continue
    print(i)
#5 is skipped but loop continues

#Used to terminate the loop entirely.
for i in range(1,11):   
    if i==5:
        break
    print(i)
#loop stops when i becomes 5

#range(1,21) skip 5,10,15
for i in range(1,21):
    if i==5 or i==10 or i==15:
        continue
    print(i)

l=[3,6,9,12,15,18]
for i in range(1,21):
    if i in l:
        continue
    print(i)