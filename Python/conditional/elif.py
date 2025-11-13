battery=int(input("Enter Battery: "))

if battery<=20:
    print("Battery low")
elif battery>=21 and battery<=80:
    print("Normal")
else:
    print("Great!")