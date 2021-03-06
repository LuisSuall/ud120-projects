#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""
from __future__ import division
import pickle
import sys
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
features_train, features_test, labels_train, labels_test = train_test_split(features, labels,test_size=0.3, random_state = 42)
### it's all yours from here forward!

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

score = accuracy_score(labels_test, pred)

print "Accuracy score:", score

# Evaluation Metrics mini-project
poi_predicted = sum(pred)
print "No of POI predicted:", poi_predicted
print "No of people on test:", len(labels_test)
print "Accuracy for \'not POI for everyone\':", 1-sum(labels_test)/len(labels_test)

true_positives = pred * labels_test
print "No of true positives:", sum(true_positives)

print "Precision score:", precision_score(labels_test, pred)
print "Recall score:", recall_score(labels_test, pred)
