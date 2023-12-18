# Write a function centroid(c) to calculate the centroid of 3D coordinates.

# Return the results as a list of floats. Round the values to two decimal places.

import numpy as np

def centroid(c):
    return np.mean(c, axis=0).round(2).tolist()