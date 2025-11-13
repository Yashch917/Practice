import pandas as pd
data={
    "Name":["Yash","Yash 2","Huda","Prasad sir","Karan Sir","Yash 3"],
    "Age":[21,43,54,23,54,54],
    "Marks":[54,63,34,64,64,42]
}
df=pd.DataFrame(data)
print("DataFrame:")
print(df)

print("\nSingle row(index 1):")
print(df.iloc[1])

print("\nMultiple row(index 0 and 2):")
print(df.iloc[[0,2]])

print("\nSingle Cell(row 0,column 2 - Marks of Amit):")
print(df.iloc[0,2])

print("\nSpecific Rows & Columns (Rows 0,2 and columns 0,2):")
print(df.iloc[[0,2],[0,2]])

print("\nRange of Rows(0 to 2):")
print(df.iloc[0:2])

print("\nRange of Rows and Columns (0:3, 0:2)")
print(df.iloc[0:3, 0:2])

df.iloc[1,2]=80
print("\nAfter modifying Ravi's Marks using iloc:")
print(df)