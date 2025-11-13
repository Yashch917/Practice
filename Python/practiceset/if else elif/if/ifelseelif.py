det=eval(input("Enter Obstacle Distance: "))

if det<=10:
    print("Stop the Robot")


dust=input("Is there dust? (yes/no): ")
if dust=="yes" or dust=="y" or dust=="Y":
    print("Start the vacuum cleaner")
else:
    print("No action needed")