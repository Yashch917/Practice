delive=input("Enter the delivery location (home/shop): ")

a=delive.lower()
if a=="home":
    print("Deliver Package")
elif a=="shop":
    print("Pick package")
else:
    print("else")