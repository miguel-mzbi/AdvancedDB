import csv
import numpy

# Reads a file. Counts the number of times a id has appeared has destiny in an edge. Stores data in a dictionary.
def getCounterFromFile(pathToFile):
    counter = {}
    with open(pathToFile) as csvfile:
        csvfile.readline()
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            nodo = row[1]
            if nodo in counter.keys():
                counter[nodo] += 1
            else:
                counter[nodo] = 1
    return counter

# Reads a file. Stores in a dictionary
def getIdNamesFromFile(pathToFile):
    idNames = {}
    with open(pathToFile) as csvfile:
        csvfile.readline()
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            idNames[row[0]] = row[1]
    return idNames

# Prints dictionary or list
def printListOrDict(item):
    if(type(item) is dict):
        for i in item.items():
            print(i)
    else:
        for t in item:
            print(t)
    return

# Returns list average
def getAverage(A):
    return numpy.average(A)

# Returns list standard deviation
def getStdDev(A):
    return numpy.std(A)

# Stores the entry of a dictionary in another one, if the value is bigger or equal to the minimum.
def getSignificantValues(A, min):
    B = {}
    t = 0
    for x in A.items():
        if(x[1] >= min):
            B[x[0]] = x[1]
        else:
            t += 1
    print(str(t) + " elements were deleted.")
    return B

# Append dictionary with anotherone with the same keys. Returns an ordered list.
def appendDics(A, B):
    completeDic = {}
    for x in A.items():
        completeDic[x[0]] = [x[1], B.get(x[0])]
    return sorted(completeDic.items(), key = lambda x : x[1][0], reverse = True) # Order in descending order.

##MAIN CODE

counter = getCounterFromFile('Esa+Nasa EDGES.csv') # Dictionary to hold the id and the number of relations where it's the destination node
idNames = getIdNamesFromFile('Esa+Nasa NODE.csv') # Get id and names

# [x[1] for x in counter.items()] makes a list of the values. Useful for operations.
average = getAverage([x[1] for x in counter.items()]) # Stores the average.
stdDev = getStdDev([x[1] for x in counter.items()]) # Stores the Standard Deviation.
myStd = stdDev/3 # Stores the range we will use as filter. In this case we will just use just one third of the standard deviation.
myMin = average-myStd # All values lesser than this will not be considered.
print("Average = " + str(average))
print("StdDev = " + str(stdDev))
print("My StdDev = " + str(myStd))
print("All numbers entries with values smaller than " + str(myMin) + " will not be considered\n")

counterSignificant = getSignificantValues(counter, myMin) # Stores id and value of nodes that passed the filter.

completeDic = appendDics(counterSignificant, idNames) # Append names to ids and values

print("Number of elements considered: " + str(len(completeDic)))
printListOrDict(completeDic)

