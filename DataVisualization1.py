import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('student.csv')
marks=data.iloc[0:,1]
names=data.iloc[0:,0]
plt.pie(marks,labels=names)
