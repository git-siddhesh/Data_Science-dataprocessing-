import matplotlib.pyplot as plt
import pandas as pd 
data=pd.read_csv('bank.csv')
#data.columns
rown=data.RowNumber
surnam=data.Surname
credit=data.CreditScore
geography=data.Geography
age=data.Age
gender=data.Gender
tenure=data.Tenure
bal=data.Balance
                                       
plt.bar(geography,bal)
plt.show()
      # NumOfProducts
      #HasCrCard   
      # IsActiveMember
      # EstimatedSalary
      # Exited


#plot all the possible graphs 
#use all possible combination of allc columns
