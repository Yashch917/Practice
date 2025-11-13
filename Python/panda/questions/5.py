# Q5. Robot Task Record

# A robot performs daily cleaning tasks 
# and logs the area cleaned (in m²):

# Day	Area_Cleaned
# Mon	120
# Tue	150
# Wed	100
# Thu	180
# Fri	160

# Tasks:

# Display first 3 records.
# Find total area cleaned in the week.
# Find the day with the maximum area cleaned.
import pandas as pd
data={
    "Day":["Mon","Tue","Wed","Thu","Fri"],
    "Area_Cleaned":[120,150,100,180,160]
}
df=pd.DataFrame(data)
print("This is the Robot Task Record DataFrame:\n",df)
print("-----------------------------------------")
print("First 3 Records:\n",df.head(3))
print("-----------------------------------------")
total=df["Area_Cleaned"].sum()
print("Total area cleaned in the week:",total,"m²")
print("-----------------------------------------")
maxday=df.loc[df["Area_Cleaned"].idxmax()]
print("Day with maximum area cleaned:\n",maxday)