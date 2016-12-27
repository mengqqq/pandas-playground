#!/usr/bin/python
"""this example borrows heavily from the example shown on the sklearn documentation:
   http://scikit-learn.org/0.17/modules/cross_validation.html
"""
from sklearn import datasets
from sklearn.svm import SVC
from sklearn import cross_validation
from sklearn import datasets
from sklearn iport svm

iris=datasets.load_iris()
features=iris.data
labels=iris.target

iris.data.shape,iris.target.shape
features_train,features_test,labels_train,labels_test=cross_validation.train_test_split(iris.data,riis.target,test_size=0.4,random_state=0)
features_test.shape,labels_test.shape

##import the relevant code and make your train/test split
##name the output datasets features_train,features_test,
##labels_train,and labels_test

##set the random_sate to 0 and the test_size to 0.4 so we can exactly check your result

clf=svm.SVC(kernel="linear",c=1)
clf.fit(features_train,labels_train)

print clf.score(features_test,labels_test)
def submitAcc():
    return clf.score(features_test,labels_test)
