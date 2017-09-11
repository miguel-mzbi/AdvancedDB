import csv

contador = {}

with open('Esa+Nasa EDGES.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        nodo = row[1]
        if row[1] in contador.keys():
            contador[nodo] += 1
        else:
            contador[nodo] = 1

            
