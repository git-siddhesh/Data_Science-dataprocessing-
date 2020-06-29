import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
df=pd.read_csv('bank.csv').head(20).drop(['RowNumber','CreditScore','Balance','CustomerId','Surname'],axis=1)
features=df.drop('EstimatedSalary',axis=1)
label=df['EstimatedSalary'].values
lageography=LabelEncoder()
lagender=LabelEncoder()
features['Geography']=lageography.fit_transform(features['Geography'])
features['Gender']=lagender.fit_transform(features['Gender'])
features=features.values
features
label
traind,testd,trainl,testl=train_test_split(features,label,test_size)
clf=DecisionTreeClassifier()
trained=clf.fit(traind,trainl)
predicts=trained.predict(testd)

accuracy_score(predicts,testl)