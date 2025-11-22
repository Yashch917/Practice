#Adding / Removing data in Pandas

#There are two types:
#Add/Remove Columns
#Add/ Remove Rows
import pandas as pd
df=pd.DataFrame({
    "Name":["Amit","Ravi","Prasad","Priya"],
    "Marks":[85,78,92,88]
})
print("\nOriginal DataFrame:\n",df)
df["Grade"]=["A","B","A+","A"]
print("\nDataFrame after adding new column:\n",df)

df["Status"]=df["Marks"]>85
print(df)