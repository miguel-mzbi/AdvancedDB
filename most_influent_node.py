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

contadorList = sorted(contador.items(), key = lambda x : x[1], reverse = True)
contadorTop3 = contadorList[:3]
print(contadorTop3)
contadorNames = []
noFound = 0
with open('Esa+Nasa NODE.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] in contadorTop3:
            contadorNames[contadorTop3.index(row[0])] = row[1]
            print(row(1))
            noFound += 1
        if noFound == 3:
            break

print(contadorNames)
