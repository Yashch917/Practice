#dataset name, marks and grade
#add result cloumn condition marks>75 pass else fail
#q2 add a row(student) using len(df) then add percentage column then remove marks column

import pandas as pd
df=pd.DataFrame({
    "Name":["Amit","Ravi","Prasad","Priya"],
    "Marks":[85,72,92,88],
    "Grade":["A","B","A+","A"]
})
print("\nOriginal DataFrame:\n",df)
#Question 1
df["Result"]=["Pass" if Marks>75 else "Fail" for Marks in df["Marks"]]
print("\n",df)

#Question 2
df.loc[len(df)] = ["Rohan", 90, "A+", "Pass"]
print("\n",df)

df["Percentage"] = (df["Marks"].astype(float) / 100) * 100
df=df.drop("Marks",axis=1)
print("\n",df)