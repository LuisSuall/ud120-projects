#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier(min_samples_split=40)

print "no of features:", len(features_train[0])

print "Training model"
time1 = time()
clf.fit(features_train, labels_train)
time2 = time()
print "Training time:",time2-time1,"s"

print "Predicting test data"
time1 = time()
pred = clf.predict(features_test)
time2 = time()
print "Predicting time:",time2-time1,"s"

print "Computing accuracy"
time1 = time()
accuracy = accuracy_score(labels_test, pred)
time2 = time()
print "Accuracy time:",time2-time1,"s"

print "Accuracy: "
print accuracy


#########################################################
