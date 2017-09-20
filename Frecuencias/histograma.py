file_path = "palabras.txt"

histograma = {}

with open(file_path, 'r') as f:
    for line in f:
        for word in line.split():
            if(word in histograma.keys()):
                histograma[word] += 1
            else:
                histograma[word] = 1

print(sorted(histograma.items(), key = lambda x : x[1], reverse = True))
