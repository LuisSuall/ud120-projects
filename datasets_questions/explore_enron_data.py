#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
from math import isnan

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print enron_data["SKILLING JEFFREY K"]

print "No of points in the dataset:", len(enron_data)

print "Features per person:", len(enron_data["GLISAN JR BEN F"])

num_POI = sum(value["poi"] for person, value in enron_data.iteritems())
print "No of POI:", num_POI

print "Stock of James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Emails from Wesley Colwell to POIs:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Stock options exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Skilling's total payment:", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Lay's total payment:", enron_data["LAY KENNETH L"]["total_payments"]
print "Fastow's total payment:", enron_data["FASTOW ANDREW S"]["total_payments"]

print "No of known salary:",sum(not isnan(float(value["salary"])) for person, value in enron_data.iteritems())
print "No of known email:",sum("NaN" not in value["email_address"] for person, value in enron_data.iteritems())

unknown_total_payments = sum(isnan(float(value["total_payments"])) for person, value in enron_data.iteritems())
print "No of unknown total payments:", unknown_total_payments
print "Percentage:", float(unknown_total_payments)/len(enron_data)

unknown_POI_total_payments = sum(isnan(float(value["total_payments"]) if value["poi"] else False) for person, value in enron_data.iteritems())
print "No of POI unknown total payments:", unknown_POI_total_payments
print "Percentage:", float(unknown_POI_total_payments)/num_POI
#for name, value in enron_data.iteritems():
#    print name, value["email_address"]
