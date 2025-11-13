inp=int(input("Enter whether the Packet is Present (yes/no): "))
a=inp.lower()

if a=="yes" or a=="y":
    print("Deliver the Packet")
else:
    print("Do not Deliver the Packet")