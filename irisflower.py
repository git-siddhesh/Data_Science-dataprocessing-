#!/usr/bin/python3
from sklearn import datasets
[i for i in dir(datasets) if 'load' in i]
# this dataset is provided by SCI-kit learn for offline

import matplotlib.pyplot as plt # for plotting graph
from sklearn.datasets import load_iris #to load dataset
from sklearn.model_selection import train_test_split #to 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# now loading irirs data only
iris=load_iris()
dir(iris)
#iris.DESCR
iris.feature_names     #Thee are the features
iris.target_names     #these are the labels
features=iris.data     #actual data with attribute
#features.shape      #(150,4)
#type(features)    #numpy.ndarray
#now time for target / label data that will be exactly same as
#no of features data
label=iris.target
#lable.shape     # (150,)
#write a program that replace the o with sentosa 1 with versicolor 2 with verginica 
sep_len=features[0:,0]  # return the first column which is sepal length
sep_wid=features[0:,1]
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.scatter(sep_len,sep_wid,label="Sepal_data",marker='*')
plt.scatter(features[0:,2],features[0:,3],label="petal_data",marker='x')
plt.legend()
#Now time for separting data into two category 
# 1. Training data 
# 2. Testing data
train_data,test_data,train_label,test_label=train_test_split(features,label,test_size=0.1)  #0.1 means 10 %
#calling decision tree classifier
clf=DecisionTreeClassifier()
trained=clf.fit(train_data,train_label)
#----------------recv.py
predicted_flowers=trained.predict(test_data)
test_label
# find accuracy score
accuracy_score(test_label,predicted_flowers)