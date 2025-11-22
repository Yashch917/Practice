import pandas as pd
data={
    "Name":["Amit","Prasad","Alok","Aaryan","Yash","Huda","Rohan","Prasad","Ravi"],
    "Marks":[30,40,50,43,99,84,75,34,66]
}
df=pd.DataFrame(data)

result=df[df["Marks"]>85]
print("\n",result)

result=df[df["Name"].str.startswith("R")]
print("\n",result)

result=df[df["Marks"].between(70,90)]
print("\n",result)

result=df[df["Name"].str.contains("e")]
print("\n",result)

result=df[(df["Marks"]>80) | (df["Name"]=="Rohan")]
print(result)