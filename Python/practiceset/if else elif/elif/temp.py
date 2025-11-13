temp=int(input("Enter the temperature: "))

if temp>=70:
    print("Shut Down the System")
elif temp>=50:
    print("High Temperature Warning")
elif temp>=30:
    print("Temperature is Normal")
else:
    print("Cool Environment")