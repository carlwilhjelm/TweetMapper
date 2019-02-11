from LocalDir import *
import pickle

with open(pairwiseRankAmbiguousTweetsListFile, 'rb') as f:
    list = pickle.load(f)

checkDict = {}
textSet = []
textResults = ""

# use a dict to check if tweet has been logged
# if not, add to list
for key, textScoreTuple in reversed(list):
    if textScoreTuple[0] not in checkDict:
        checkDict[textScoreTuple[0]] = True
        textSet.append(textScoreTuple)

for elem in textSet:
    textResults += str(elem) + "\n"

with open(pairwiseRankSetAmbiguousTweetsTextResultsFile, 'w') as f:
    f.write(textResults)

with open(pairwiseRankSetAmbiguousTweetsListFile, 'wb') as f:
    pickle.dump(textSet, f)

