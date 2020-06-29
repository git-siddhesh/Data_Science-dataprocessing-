
fileformat='csv'
csf1='dtc'
filepath='bank.csv'
import pandas as pd 
#reading data of the respective file format
if fileformat=='csv':
    df=pd.read_csv(filepath)
    print(df.head())

targetcol=input("Enter targetcol")

#--------------------------------
if csf1=='dtc':
    from sklearn.tree import DecisionTreeClassifier
    clf=DecisionTreeClassifier()
    x=df.drop([targetcol],axis='columnst')
    y=df.target
    print(x)
    print(y)
