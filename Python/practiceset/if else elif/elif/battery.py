batt=int(input("Enter the Battery Percentage: "))

if batt>=80:
    print("Battery is Full")
elif batt>=50:
    print("Half Charged")
elif batt>=20:
    print("Low Battery")
else:
    print("Critical Battery")