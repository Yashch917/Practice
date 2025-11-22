import pandas as pd
data={
    "Name":["Amit","Prasad","Alok","Aaryan"],
    "Marks":[30,40,50,43]
}
df=pd.DataFrame(data)

result=df[df["Marks"].between(30,40)]
print("\n",result)