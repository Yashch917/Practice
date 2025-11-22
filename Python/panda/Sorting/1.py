# 6. Sorting Data in Pandas
# There are two main functions:

# | Function        | Purpose                                |
# | --------------- | -------------------------------------- |
# | `sort_values()` | Sorts DataFrame based on column values |
# | `sort_index()`  | Sorts DataFrame based on index numbers |

# A) sort_values() Example

import pandas as pd
df=pd.DataFrame({
    "Name":["Amit","Ravi","Prasad","Priya"],
    "Marks":[85,72,92,88],
    "Grade":["A","B","A+","A"]
})
print("\nOriginal DataFrame:\n",df)

print("\nSorted by Marks(Ascending:)\n",df.sort_values("Marks"))
print("\nSorted by Marks(Descending:)\n",df.sort_values("Marks",ascending=False))
print("\nSorted by Index(Descending:)\n",df.sort_index(ascending=False))