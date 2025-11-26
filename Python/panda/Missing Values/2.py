#What is fillna()?

#fillna() is used to replace missing values (NaN) with a specified value.
#with some meaningful data.
import pandas as pd

df=pd.DataFrame({
    "Name":[None,"Ravi","Prasad","Priya"],
    "Age":[21,None,22,20],
    "Marks":[85,78,None,88]
})
print("\nOriginal DataFrame:\n",df)
print("\nDataFrame after filling missing values with 0:\n",df.fillna(0))

#Replace missing values in a specific column
df2=df.copy()
print("\nDataFrame after filling Marks missing values with Middle Value:\n")
df2["Marks"]=df2["Marks"].fillna(df2["Marks"].median())
print(df2)

print("\nDataFrame after filling Age missing values with Mean:\n")
df2["Age"]=df2["Age"].fillna(df2["Age"].mean())
print(df2)