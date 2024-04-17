import csv
import copy

# Define a dictionary for vehicle properties
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Print initial dictionary values
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))