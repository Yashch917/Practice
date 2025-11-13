#using random variable simulate robot obstacle detection
#if robot detects obstacle then turn left or right randomly
#if no obstacle move forward
#total distance is 5,20 meter using random variable

import random
distance = random.randint(5,20)
directions=["left","right","forward"]
print(f"Robot starting mission for {distance} meters.")
for meter in range(1,distance+1):
    obstacle=random.choice([True,False])
    if obstacle:
        turn=random.choice(directions[:2]) #left or right
        print(f"Meter {meter}: Obstacle detected! Turning {turn}.")
    else:
        print(f"Meter {meter}: Path clear. Moving forward.")
print("Mission completed.")