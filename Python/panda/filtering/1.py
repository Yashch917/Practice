#Filtering Data in Pandas:--->
#Filtering means selecting only those rows that match a certain condition.
#Just like SQL WHERE or Python if, but applied to an DataFrame.

#1.Basic Filtering (Single Condition)
import pandas as pd
data={
    "Name":["Amit","Prasad","Alok","Aaryan"],
    "Marks":[30,40,50,43]
}
df=pd.DataFrame(data)
print(df[df["Marks"]>35])