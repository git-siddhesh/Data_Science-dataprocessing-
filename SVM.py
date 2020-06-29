    from sklearn.datasets import load_digits
digit=load_digits()
features=digit.data
label=digit.target
from sklearn.model_selection import train_test_split
X,x,Y,y=train_test_split(features,label,test_size=0.2)
import matplotlib.pyplot as plt
plt.imshow(digit.images[0])

from sklearn.svm import SVC
clf=SVC(gamma=100)
trained=clf.fit(X,Y)
#now time for prediction
output=trained.predict(x)
from sklearn.metrics import accuracy_score
accuracy_score(output,y)

# as kernel and the gamma changes the accuracy score also changes
# read the kernels and gamma

#random forest
#name bages

# what is ensamble ?
