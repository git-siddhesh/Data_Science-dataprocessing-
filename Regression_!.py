# to create an ideal model 
''' Types of regression 
   1. Linear
    a. single independent 
    b. multipl independent
        y= a1 + a2x2 + ... 
   2. Polynomial 
   2. Logistical

Y = b0 + b1X
'''
import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('salary.csv')
# salary = b0 + b1*experience

# experience that we are going to use as input of training data
exp=df.iloc[:,0].values

# actual salary
sal = df.iloc[:.1]

# now we can visualize this exp and sal data
plt.xlabel("Experience")
plt.ylabel("salary")
plt.scatter(exp,sal)
plt.show()