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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "enron data length:", len(enron_data)
print "feature count:", len(enron_data['METTS MARK'])

poi_count = 0
for k, v in enron_data.items():
    if v["poi"] == 1:
        poi_count += 1

print "poi_count:",poi_count

print "James Prentice's total_stock_value:",enron_data['PRENTICE JAMES']['total_stock_value']

print "form Wesley Colwell to poi:",enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "SKILLING JEFFREY's exercised_stock_options :",\
    enron_data['SKILLING JEFFREY K']['exercised_stock_options']
