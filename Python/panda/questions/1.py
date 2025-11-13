# Q1. Robot Battery Data
# Create a DataFrame to store battery levels (in %) of 4 robots recorded at morning and evening:

# Robot	    Morning	    Evening
# R1	      90	      60
# R2	      80	      55
# R3	      85	      65
# R4	      95	      70

# Tasks:
# Print only the Morning column.
# Find the average battery usage of all robots (Morning - Evening).
# Add a new column ‘Battery_Used’ = Morning - Evening.

import pandas as pd
data={
    "Robot":["R1","R2","R3","R4"],
    "Morning":[90,80,85,95],
    "Evening":[60,55,65,70]
}
df=pd.DataFrame(data)
print("This is the Robot Battery DataFrame:\n",df)
print("-----------------------------------------")
print("Printing morning column:\n",df['Morning'])
print("-----------------------------------------")
df['Battery_Used']=df['Morning']-df['Evening']
print("DataFrame after adding Battery_Used column:\n",df)
average_battery_usage=df['Battery_Used'].mean()
print("-----------------------------------------")
print("Average battery usage of all robots:",average_battery_usage)
print("-----------------------------------------")