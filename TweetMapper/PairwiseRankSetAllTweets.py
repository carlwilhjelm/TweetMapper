from LocalDir import *
import pickle

with open(pairwiseRankAllTweetsListFile, 'rb') as f:
    list = pickle.load(f)

checkDict = {}
textSet = []
textResults = ""

# use a dict to check if tweet has been logged
# if not, add to list format textSet[key] = [text, score]
for score, tokens, ID in reversed(list):
    text = " ".join(tokens)
    if text not in checkDict:
        checkDict[text] = True
        textSet.append([score, tokens, ID])

for elem in textSet:
    textResults += str(elem) + "\n"

with open(pairwiseRankSetAllTweetsResultsFile, 'w', encoding=twitterEncoding) as f:
    f.write(textResults)

with open(pairwiseRankSetAllTweetsListFile, 'wb') as f:
    pickle.dump(textSet, f)

