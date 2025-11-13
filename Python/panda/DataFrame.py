import pandas as pd 
data={
    "Name":["Yash","Huda","Prasad sir","Yash k","Karan Sir"],
    "Age":[21,34,54,65,43],
    "Marks":[55,44,66,77,44],
    "School":["ABC","DEF","GHI","JKL","MNO"],
    "City":["Pune","Mumbai","Delhi","Bangalore","Chennai"]
}
df=pd.DataFrame(data)
print("This is the panda DataFrame:\n",df)