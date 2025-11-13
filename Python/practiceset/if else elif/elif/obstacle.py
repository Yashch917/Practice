obs=eval(input("Enter Obstacle Distance (cm): "))

if obs<=5:
    print("Stop the Robot")
elif obs<=15:
    print("Slow Down Robot")
else:
    print("Move Fast")