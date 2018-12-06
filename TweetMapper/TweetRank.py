from LocalDir import *
import pickle


# object file for dictionary of original tweets
originalTweetsFile = localDir + "AllTweetsTextOnlyDictObj.txt"

# object file for tokenized unambiguous tweets
unambiguousTokenizedTweetsFile = localDir + "UnambiguousTokenizedTweetsDictObj.txt"
# object file for tokenized ambiguous tweets
ambiguousTokenizedTweetsFile = localDir + "AmbiguousTokenizedTweetsDictObj.txt"

# object file for relative frequency dictionary
relFreqDictFile = localDir + "RelFreqDictObj.txt"

# where text of all results is stored
outAllTextResultsFile = localDir + "TweetRankAllTextResults.txt"
# output file for all Tweet Rank dictionary
outAllDictFile = localDir + "AllTweetRankDictObj.txt"
# output file for all Tweet Rank list
outAllListFile = localDir + "AllTweetRankListObj.txt"

# where text of unambiguous results is stored
outUnambiguousTextResultsFile = localDir + "TweetRankUnambiguousTextResults.txt"
# output file for unambiguous Tweet Rank dictionary
outUnambiguousDictFile = localDir + "UnambiguousTweetRankDictObj.txt"
# output file for unambiguous Tweet Rank list
outUnambiguousListFile = localDir + "UnambiguousTweetRankListObj.txt"

# where text of unambiguous results is stored
outAmbiguousTextResultsFile = localDir + "TweetRankAmbiguousTextResults.txt"
# output file for unambiguous Tweet Rank dictionary
outAmbiguousDictFile = localDir + "AmbiguousTweetRankDictObj.txt"
# output file for unambiguous Tweet Rank list
outAmbiguousListFile = localDir + "AmbiguousTweetRankListObj.txt"

# load dictionary of origional tweet text
with open(originalTweetsFile, 'rb') as f:
    originalTweets = pickle.load(f)

# load tokenized tweets
with open(unambiguousTokenizedTweetsFile, 'rb') as f:
    unambiguousTokenizedTweets = pickle.load(f)
with open(ambiguousTokenizedTweetsFile, 'rb') as f:
    ambiguousTokenizedTweets = pickle.load(f)

# load relative frequency dictionary
with open(relFreqDictFile, 'rb') as f:
    relFreq = pickle.load(f)

with open(unambiguousWordsListFile, 'rb') as f:
    unambiguousDictionary = pickle.load(f)

textAllResults = ""
textUnambiguousResults = ""
textAmbiguousResults = ""
allTweetRank = {}
unambiguousTweetRank = {}
ambiguousTweetRank = {}

def setRank(tweetSetIn):
    setRankOut = {}
    for ID, text in tweetSetIn.items():
        setRankOut[ID] = [originalTweets[ID], 0]
        for s in text:
            setRankOut[ID][1] += relFreq[s]
        setRankOut[ID][1] /= len(text)
    return setRankOut

unambiguousTweetRank = setRank(unambiguousTokenizedTweets)
ambiguousTweetRank = setRank(ambiguousTokenizedTweets)
allTweetRank = unambiguousTweetRank.copy()
allTweetRank.update(ambiguousTweetRank)

allSortedByValue = sorted(allTweetRank.items(), key=lambda kv: kv[1][1])
for key, val in allSortedByValue:
    textAllResults += (key + ":   " + str(val[1]) + ":   " + val[0] + '\n')

unambiguousSortedByValue = sorted(unambiguousTweetRank.items(), key=lambda kv: kv[1][1])
for key, val in unambiguousSortedByValue:
    textUnambiguousResults += (key + ":   " + str(val[1]) + ":   " + val[0] + '\n')

ambiguousSortedByValue = sorted(ambiguousTweetRank.items(), key=lambda kv: kv[1][1])
for key, val in ambiguousSortedByValue:
    textAmbiguousResults += (key + ":   " + str(val[1]) + ":   " + val[0] + '\n')

with open(outAllTextResultsFile, 'w') as f:
    f.write(textAllResults)

with open(outAllDictFile, 'wb') as f:
    pickle.dump(allTweetRank, f)

with open(outAllListFile, 'wb') as f:
    pickle.dump(allSortedByValue, f)

with open(outUnambiguousTextResultsFile, 'w') as f:
    f.write(textUnambiguousResults)

with open(outUnambiguousDictFile, 'wb') as f:
    pickle.dump(unambiguousTweetRank, f)

with open(outUnambiguousListFile, 'wb') as f:
    pickle.dump(unambiguousSortedByValue, f)

with open(outAmbiguousTextResultsFile, 'w') as f:
    f.write(textAmbiguousResults)

with open(outAmbiguousDictFile, 'wb') as f:
    pickle.dump(ambiguousTweetRank, f)

with open(outAmbiguousListFile, 'wb') as f:
    pickle.dump(ambiguousSortedByValue, f)
