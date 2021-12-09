from math import *
import csv

# read sample files
def read_csv_file(file_name):
    """This function reads csv files into a list
    :param file_name:    name of the file to be read into a list
    :param return:       returns the data in a list format"""
    with open(file_name) as file:
        reader = csv.read(file)
        data = []
        for row in reader:
            data.append(row)
    return data

#read data 
data1 = read_csv_file('data1.csv')
data2 = read_csv_file('data2.csv')
weights = read_csv_file('weights.csv')
sample1 = read_csv_file('samples1.csv')
sample2 = read_csv_file('samples2.csv')

def results_func(data_set_1, data_set_2, weights):
    """Computes the results based on their weights
    :param data_set_1:     the data set to be substracted to 
    :param data_set2:      the data set that will be subtracted
    :param weights:        the specific weight of the difference
    :param return:         returns the weighted results 
    """
    results = []
    for i in range(len(data_set_1)):
        s = 0
        for j in range(len(weights)):
            d = data_set_1[i][j] - data_set_2[i][j]
            s += weights[j] * abs(d)
        results.append(s)
    return results 

results1 = results_func(data1, data2, weights)
critical = 0
for i in range(len(results1)):  # for all i
    if results1[i] > 5:
        critical = critical + 1  # increase by 1

print("criticality:", critical, "results above 5")

results2 = results_func(sample1, sample2, weights)
dsum =  0
for i in range(len(results2)):
    dsum = dsum + results2[i]
print("d-index:", dsum/len(results2))
