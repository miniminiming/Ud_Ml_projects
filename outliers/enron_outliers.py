#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
#remove biggest data
data_dict.pop('TOTAL',0)
features = ["salary", "bonus"]
# print data_dict
data = featureFormat(data_dict, features)


### your code below


#the biggest salary
salary_biggest = []
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus )
    if salary > 1000000 and bonus>5000000:
        salary_biggest.append(point)

for k,v in data_dict.items():
    for point in salary_biggest:
        if v['salary'] == point[0]:
            print "rich man:",k


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

