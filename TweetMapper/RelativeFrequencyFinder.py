from LocalDir import *
from collections import defaultdict
import nltk
import pickle

# object file for all tweets
allTweetsFile = localDir + "AllTokenizedTweetsDictObj.txt"
# object file for unambiguous tweets
unambiguousTweetsFile = localDir + "UnambiguousTokenizedTweetsDictObj.txt"
# where text reference of results is stored
outTextFile = localDir + "RelFreqTextResults.txt"
# where results sorted list obj is stored
outListFile = localDir + "RelFreqListObj.txt"
# where results dict obj is stored
outDictFile = localDir + "RelFreqDictObj.txt"

# takes file object of list of strings (tweets) and returns frequency value for each word
# wordCount/numberOfTweets
def frequencyFinder(fileNameIn):
    frequency = defaultdict(int)
    with open(fileNameIn, 'rb') as f:
        tweets = pickle.load(f)

    for ID, text in tweets.items():
        for word in text:
            frequency[word] += 1

    length = len(tweets)

    for key in frequency:
        frequency[key] /= length

    return frequency


allTweetsFrequency = frequencyFinder(allTweetsFile)
unambiguousTweetsFrequency = frequencyFinder(unambiguousTweetsFile)

relativeFrequency = {}
for key in allTweetsFrequency:
    relativeFrequency[key] = unambiguousTweetsFrequency[key] / allTweetsFrequency[key]

sortedByValue = sorted(relativeFrequency.items(), key=lambda kv: kv[1])
textResults = ""

for elem in sortedByValue:
    textResults += str(elem) + "\n"

with open(outTextFile, 'w') as f:
    f.write(textResults)

with open(outListFile, 'wb') as f:
    pickle.dump(sortedByValue, f)

with open(outDictFile, 'wb') as f:
    pickle.dump(relativeFrequency, f)
