import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
cancer=load_breast_cancer()
dir(load_breast_cancer())
#['DESCR', 'data', 'feature_names', 'target', 'target_names']
#cancer.feature_names
#cancer.target_names
features=cancer.data
labels=cancer.target
size=float(input("Enter the test size in float"))
traindata,testdata,trainlabel,testlabel=train_test_split(features,labels,train_size=size)
classifier=input("Enter the classifier name")
def()