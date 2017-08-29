import stop_words
import json

words_path = "palabras.txt"
similarDic_path = "diccionarioSimilares.json"

#Reads a txt all as a list, all in lowercase. Italso removes punctuations
def readWordsFile(wordlist):
    with open(words_path, 'r') as f:
        for line in f:
            linelist = stop_words.removePunctuations(line, stop_words.punctuations)
            wordlist += linelist.lower().split()
    return wordlist

#Convert raw list of words to a dictionary with the word as key and the frequency as value.
#Stop words are removed
#Misspelled words are replaced
#Returns a dictionary
def wordListToFreqDict(wordlist):
    wordlist_proc = stop_words.removeStopwords(wordlist, stop_words.stopwords + ['t'])
    with open(similarDic_path) as jsonData:
        jsonDict = json.load(jsonData)
        for i in range(len(wordlist_proc)):
            if wordlist_proc[i] in jsonDict:
                wordlist_proc[i] = jsonDict[wordlist_proc[i]]

    wordfreq = [wordlist_proc.count(p) for p in wordlist_proc]
    return dict(zip(wordlist_proc,wordfreq))

#Orders words in descending order
def orderDictByValuesToList(dictionary):
    return sorted(dictionary.items(), key = lambda x : x[1], reverse = True)
#Prints dictionary or list
def printListOrDict(item):
    if(type(item) is dict):
        for i in item.items():
            print(i)
    else:
        for t in item:
            print(t)

wordlist = []
frequencyDictionary = {}

wordlist = readWordsFile(wordlist)
frequencyDictionary = wordListToFreqDict(wordlist)
orderedFreqList = orderDictByValuesToList(frequencyDictionary)

printListOrDict(orderedFreqList)
