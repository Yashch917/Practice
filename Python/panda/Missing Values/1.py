# What is Missing Data?
# Missing data means some values are empty, blank, unavailable, or not recorded.
# In Pandas, missing data is represented as: NaN (Not a Number).

# Example:
# | Name  | Age | Marks |
# | ----- | --- | ----- |
# | Amit  | 21  | 85    |
# | Ravi  | NaN | 78    |
# | Sneha | 20  | NaN   |
# Here, Ravi’s Age and Sneha’s Marks are missing → NaN

import pandas as pd

df=pd.DataFrame({
    "Name":["Amit","Ravi","Prasad","Priya"],
    "Age":[21,None,22,20],
    "Marks":[85,78,None,88]
})
print("\nOriginal DataFrame:\n",df)

# Detect Missing Data
# Function	Meaning
# df.isnull()	Shows True where data is missing
# # df.notnull()	Shows True where data is available
print("\nNull Values\n",df.isnull())
print("\nNot Null Values\n",df.notnull())

print("\nNull Values Count\n",df.isnull().sum())

print("\nDrop Null Values\n",df.dropna())
print("\nDrop Null Values Column\n",df.dropna(axis=1))

print("\nAll Values\n",df.dropna(how="all"))

mdf=df[df.isnull().any(axis=1)]
print("\nRows with Missing Values\n",mdf)

cdf=df[df.notnull().all(axis=1)]
print("\nRows without Missing Values\n",cdf)