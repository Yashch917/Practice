#1. Accessing Data in DataFrame
#We can access specific rows, columns, or cells using two main methods:
#loc[] -> Label-based Access
#iloc[]-> Index-based access

import pandas as pd
data={
    "Name":["Yash","Yash 2","Huda","Prasad sir","Karan Sir","Yash 3"],
    "Age":[21,43,54,23,54,54],
    "Marks":[54,63,34,64,64,42]
}
df=pd.DataFrame(data,index=["R1","R2","R3","R4","R5","R6"])
print("DataFrame:")
print(df)

print("\nSingle row(R2):")
print(df.loc['R2'])

print("\nMultiple row(R1,R3):")
print(df.loc[['R1','R3']])

print("\nSingle Cell(Marks of R1):")
print(df.loc['R1','Marks'])

print("\nSpecific Rows & Columns (R1 & R3, Name & Marks):")
print(df.loc[['R1','R3'],['Name','Marks']])

print("\nRange of Rows(R1 to R3):")
print(df.loc['R1':'R3'])

print("\nConditional Selection (Marks > 50):")
print(df.loc[df['Marks']>50])

df.loc['R2','Marks']=80
print("\nAfter modifying Ravi's Marks using loc:")
print(df)