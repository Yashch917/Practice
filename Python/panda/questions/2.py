# Q2. Sensor Data Recording
# Create a Pandas Series for a temperature 
# sensor that records readings at 5 time intervals:
# [28.5, 29.1, 30.0, 29.6, 28.9]

# Tasks:
# Give custom index labels as time: T1, T2, T3, T4, T5.
# Find the maximum and minimum temperature.
# Change the reading at T3 to 31.0.
import pandas as pd
temp = pd.Series([28.5, 29.1, 30.0, 29.6, 28.9],
index=['T1', 'T2', 'T3', 'T4', 'T5'])
print("Temperature Series:\n", temp)
print("-----------------------------------------")
print("Maximum Temperature:", temp.max())
print("Minimum Temperature:", temp.min())
print("-----------------------------------------")
temp["T3"]=31.0
print("Updated Temperature Series after changing T3 to 31.0:\n", temp)