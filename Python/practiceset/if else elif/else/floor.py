flo=input("Enter whether the floor is wet or not (yes/no): ")

a=flo.lower()
if a=="yes" or a=="y":
    print("Do not move")
else:
    print("Safe to move")