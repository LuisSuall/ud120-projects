#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='rbf', C = 10000)

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

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

print "Predicted label for element 10:", pred[10]
print "Predicted label for element 26:", pred[26]
print "Predicted label for element 50:", pred[50]

import numpy as np
print "Number of elements predicted as \"Chris\" (1) class:", np.count_nonzero(pred)
#########################################################
