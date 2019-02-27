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


#scale train data length
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 


#########################################################
### your code goes here ###
import numpy as np
X = features_train
y = labels_train
from sklearn.svm import SVC
# clf = SVC(kernel = 'linear')
clf = SVC(kernel = 'rbf', C = 10000)


#big data set training time is 135.8,predict is 14.673  score 0.984
#small data set training time is 0.074,predict is 0.8 score 0.884
t0 = time()
clf.fit(X, y)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
prdice_res = clf.predict(features_test)
print "predice time:", round(time()-t0, 3), "s"

print "score:",clf.score(features_test,labels_test)

print prdice_res[10],"  ",prdice_res[26],"  ",prdice_res[50]

print "1 sum",prdice_res.sum()

#########################################################


