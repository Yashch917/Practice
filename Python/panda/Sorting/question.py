# Sort the DataFrame by Age in descending order
# Sort the DataFrame by Name alphabetically
# Sort using multiple columns: first by Result, then by Marks.

import pandas as pd
df=pd.DataFrame({
    "Name":["Amit","Ravi","Prasad","Priya"],
    "Marks":[85,72,92,88],
    "Age":[12,34,2,55]
})

df["Result"]=["Pass","Fail","Pass","Pass"]
print("\nOriginal DataFrame:\n",df)
print("\nSorted by Age(Descending):\n",df.sort_values("Age",ascending=False))
print("\nSorted by Name:\n",df.sort_values("Name"))
print("\nSorted by Result and Marks:\n",df.sort_values(["Result","Marks"]))