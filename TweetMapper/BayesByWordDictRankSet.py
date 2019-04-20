from LocalDir import *
import pickle

with open(sortedPredictionsListsByWordFile, 'rb') as f:
    sortedPredictionsByWordDict = pickle.load(f)

textResults = ""

wordDictRankSet = {}

# use a dict to check if tweet has been logged
# if not, add to list
for key, listOfTokens in sortedPredictionsByWordDict.items():
    checkDict = {}
    textSet = []
    for line in listOfTokens:
        tokens = line[1]
        text = " ".join(tokens)
        if text not in checkDict:
            checkDict[text] = True
            textSet.append(line)
    textSet.reverse()
    wordDictRankSet[key] = textSet

with open(sortedPredictionsSetsByWordFile, 'wb') as f:
    pickle.dump(wordDictRankSet, f)

setSizes = []
for word, list_ in wordDictRankSet.items():
    setSizes.append((len(list_), word))

setSizes.sort(key=lambda x: x[0], reverse=True)

textResults = ""
for line in setSizes:
    textResults += str(line) + '\n'

with open(trainingDataSetSizesTextFile, 'w') as f:
    f.write(textResults)

with open(trainingDataSetSizesListFile, 'wb') as f:
    pickle.dump(setSizes, f)
