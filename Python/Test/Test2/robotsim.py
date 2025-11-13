#Robot Battery Simulator
#Scenario: Simulate a robot's battery drain during a simple mission.
#Requirements: Create a script that starts with initial battery (int: 100%) and drains it randomly (using random module) by 1-5% per "step" (loop 10 times). Use conditionals to check if battery <20% (print warning).
#Log start/end times using datetime. Use operators for calculations and string slicing to format logs like "Battery:XX% at TIME".
#Expected Behavior: Prints 10 steps with battery levels, warnings if low, and time delta.

import random
from datetime import datetime
battery = 100
print("Robot Battery Simulator Started")
start_time = datetime.now()
print(f"Start Time: {start_time.strftime('%H:%M:%S')}")
for step in range(1,11):
    drain=random.randint(1,20)
    battery -= drain
    current_time = datetime.now()
    time_str = current_time.strftime('%H:%M:%S')
    print(f"Step {step}: Battery: {battery}% at {time_str}")
    if battery < 20:
        print("Warning: Battery low!")
    if battery <= 0:
        print("Battery depleted. Mission aborted.")
        break
    