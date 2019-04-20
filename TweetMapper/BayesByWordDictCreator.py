# create a dictionary of lists for each word, sorted by most likely to be about drugs
from LocalDir import *
from collections import defaultdict
import pickle

with open(sortedBayesPredictionsListFile, 'rb') as f:
    sortedPredictions = pickle.load(f)

with open(allWordsListFile, 'rb') as f:
    wordsList = pickle.load(f)

sortedPredictionsByWordDict = defaultdict(list)

for word in wordsList:
    sortedPredictionsByWordDict[word]

for line in sortedPredictions:
    tokens = line[1]
    for word in wordsList:
        if word in tokens:
            sortedPredictionsByWordDict[word].append(line)

with open(sortedPredictionsListsByWordFile, 'wb') as f:
    pickle.dump(sortedPredictionsByWordDict, f)

listSizes = []
for word, list_ in sortedPredictionsByWordDict.items():
    listSizes.append((len(list_), word))

listSizes.sort(key=lambda x: x[0], reverse=True)

textResults = ""
for line in listSizes:
    textResults += str(line) + '\n'

with open(trainingDataSizesTextFile, 'w') as f:
    f.write(textResults)

with open(trainingDataSizesListFile, 'wb') as f:
    pickle.dump(listSizes, f)

