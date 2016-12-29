#!/usr/bin/python

import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    errors = np.power(predictions - net_worths,2)

    order = np.argsort(errors, axis = 0)

    # Keep the 90% best fitted results
    order = order[:int(len(order)*0.9)]

    for idx in order:
        cleaned_data.append([ages[idx],
                             net_worths[idx],
                             errors[idx]])

    return cleaned_data
