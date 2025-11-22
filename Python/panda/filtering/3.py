import pandas as pd
data={
    "Name":["Amit","Prasad","Alok","Aaryan"],
    "Marks":[30,40,50,43]
}
df=pd.DataFrame(data)
result=df[(df["Marks"]>30) & (df["Name"].str.startswith("P"))]
print(result)

result=df[(df["Marks"]>30) | (df["Marks"]<50)]
print(result)