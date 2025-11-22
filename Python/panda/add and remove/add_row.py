import pandas as pd
df=pd.DataFrame({
    "Name":["Amit","Ravi","Prasad","Priya"],
    "Marks":[85,78,92,88]
})
print("\nOriginal DataFrame:\n",df)
df.loc[4]=["Rohan",90]
print(df)

df=df.drop(2)
print(df)