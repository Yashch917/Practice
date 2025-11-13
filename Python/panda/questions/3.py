# Q3. Robot Speed Tracking

# You have the following data of robots moving on a test track:

# Robot	    Speed(km/h)
# R1	        12
# R2	        15
# R3	        10
# R4	        14

# Tasks:

# Display only robots with speed > 12.
# Add a new robot R5 with speed 11.
# Sort all robots by speed (ascending).
import pandas as pd
data={
    "Robot":["R1","R2","R3","R4"],
    "Speed(km/h)":[12,15,10,14]
}
df=pd.DataFrame(data)
print("This is the Robot Speed DataFrame:\n",df)
print("-----------------------------------------")
fildf=df[df["Speed(km/h)"]>12]
print("Robots with speed greater than 12 km/h:\n",fildf)
print("-----------------------------------------")
df.loc[len(df)] = ["R5", 11]
print("DataFrame after adding R5 with speed 11 km/h:\n",df)
print("-----------------------------------------")
sortdf=df.sort_values(by="Speed(km/h)")
print("DataFrame sorted by Speed (ascending):\n",sortdf)