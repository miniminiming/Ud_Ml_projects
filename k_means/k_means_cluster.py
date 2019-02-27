#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2  in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
import numpy as np
X = finance_features
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

pred = kmeans.predict(X)

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"


# finance_features = sorted(finance_features, key=lambda datas: datas[1])
# print "first",finance_features[0]
# print "end",finance_features[len(finance_features)-1]

#use numpy find max and min value

all_data = np.array(data)
#remove zero data
exercised_stock_options = all_data[all_data[:,2] > 0]
# exercised_stock_options[:,2] means get the second column data,this is we want
print "max exercised_stock_options:",exercised_stock_options[:,2].max(axis = 0)
print "min exercised_stock_options:",exercised_stock_options[:,2].min(axis = 0)

salary = all_data[all_data[:,1] > 0]
print "max salary:",salary[:,1].max(axis = 0)
print "min salary:",salary[:,1].min(axis = 0)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
# print finance_features
scaler.fit(finance_features)
print scaler.transform([[200000.,1000000.]])