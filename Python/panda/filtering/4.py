import pandas as pd
data={
    "Name":["Amit","Prasad","Alok","Aaryan"],
    "Marks":[30,40,50,43]
}
df=pd.DataFrame(data)

result=df[df["Name"].str.contains("a")]
print("\n",result)

result=df[df["Name"].str.startswith("S")]
print("\n",result)

result=df[df["Name"].str.startswith("i")]
print("\n",result)