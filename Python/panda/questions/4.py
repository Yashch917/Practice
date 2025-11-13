# Q4. Arm Movement Angles
# Robot arm recorded angles (in degrees) during an operation:
# Time	Arm1	Arm2	Arm3
# T1	30	    45	    60
# T2	40	    55	    70
# T3	35	    50	    65

# Tasks:
# Display only the Arm2 column.
# Print the angles recorded at time T2.
# Find the average angle of each arm.
import pandas as pd
data={
    "Time":["T1","T2","T3"],
    "Arm1":[30,40,35],
    "Arm2":[45,55,50],
    "Arm3":[60,70,65]
}
df=pd.DataFrame(data)
print("This is the Robot Arm Angles DataFrame:\n",df)
print("-----------------------------------------")
print("Arm2 column:\n",df["Arm2"])
print("-----------------------------------------")
t2=df[df["Time"]=="T2"]
print("Angles recorded at time T2:\n",t2)
print("-----------------------------------------")
avg=df[["Arm1","Arm2","Arm3"]].mean()
print("Average angle of each arm:\n",avg)