'''
reading external files(csv,excel,json)
to read csv=pd.read_csv()
csv=comma separated values
looks like simpler excel
for accessing csv file, open the specific csv 
'''
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("robo.csv")
print(df)
df=pd.read_csv("robo.csv",usecols=["Battery Percentage","Robot ID"])
print(df)
df.plot()
plt.show()