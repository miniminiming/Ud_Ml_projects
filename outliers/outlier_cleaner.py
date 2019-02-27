#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    # import numpy as np
    # cleaned_data = np.concatenate((predictions, ages, net_worths, abs(net_worths-predictions)), axis = 1)
    # cleaned_data = cleaned_data[np.argsort(cleaned_data[:,3])]
    # return cleaned_data[:int(len(cleaned_data)*.9),1:]
    cleaned_data =[]
    for i in range(len(ages)):
        cleaned_data.append((ages[i],net_worths[i],(predictions[i]-net_worths[i])**2))
    #sort and remove 10% biggest data
    from operator import itemgetter, attrgetter
    cleaned_data = sorted(cleaned_data,key = itemgetter(2))
    cleaned_data = cleaned_data[0:int(len(cleaned_data)*0.9)]
    return cleaned_data

