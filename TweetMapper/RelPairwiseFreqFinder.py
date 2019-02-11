# takes file of ambiguous tweets sorted by relative frequency rank and outputs a set

from LocalDir import *
from collections import defaultdict
import pickle

# takes file object of list of strings (tweets) and returns frequency value for each word
# wordCount/numberOfTweets
def frequencyFinder(fileNameIn):
    frequency = defaultdict(int)
    with open(fileNameIn, 'rb') as f:
        tweets = pickle.load(f)

    for ID, text in tweets.items():
        try:
            if len(text) > 1:
                for i in range(len(text) - 1):
                    frequency[(text[i], text[i+1])] += 1
            else:
                frequency[("Single Word Tweet", text[0])] += 1
        except Exception as e:
            print(str(e) + '\n' + ID + '\n' + text)

    length = len(tweets)
    for key in frequency:
        frequency[key] /= length

    return frequency


allTweetsFrequency = frequencyFinder(allTokenizedTweetsDictFile)
unambiguousTweetsFrequency = frequencyFinder(unambiguousTokenizedTweetsDictFile)

relativeFrequency = {}
for key in allTweetsFrequency:
    relativeFrequency[key] = unambiguousTweetsFrequency[key] / allTweetsFrequency[key]

sortedByValue = sorted(relativeFrequency.items(), key=lambda kv: kv[1])
textResults = ""

for elem in sortedByValue:
    textResults += str(elem) + "\n"

with open(pairwiseRelFreqTextResultsFile, 'w') as f:
    f.write(textResults)

with open(pairwiseRelFreqListFile, 'wb') as f:
    pickle.dump(sortedByValue, f)

with open(pairwiseRelFreqDictFile, 'wb') as f:
    pickle.dump(relativeFrequency, f)
