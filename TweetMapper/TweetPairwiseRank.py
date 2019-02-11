from LocalDir import *
import pickle

# load dictionary of origional tweet text
with open(textByIdDictFile, 'rb') as f:
    originalTweets = pickle.load(f)

# load tokenized tweets
with open(unambiguousTokenizedTweetsDictFile, 'rb') as f:
    unambiguousTokenizedTweets = pickle.load(f)

with open(ambiguousTokenizedTweetsDictFile, 'rb') as f:
    ambiguousTokenizedTweets = pickle.load(f)

# load relative frequency dictionary
with open(pairwiseRelFreqDictFile, 'rb') as f:
    relFreq = pickle.load(f)

with open(unambiguousWordsListFile, 'rb') as f:
    unambiguousDictionary = pickle.load(f)

textAllResults = ""
textUnambiguousResults = ""
textAmbiguousResults = ""
allTweetRank = {}
unambiguousTweetRank = {}
ambiguousTweetRank = {}

# rank tweets from @param loaded tweet by ID dictionary object
def setRank(tweetSetIn):
    resultDict = {}
    for ID, text in tweetSetIn.items():
        n = len(text)
        # if tweet has a length of 1 or fewer assign score of -1
        try:
            if n > 1:
                resultDict[ID] = [originalTweets[ID], 0]
                # rank equals sum of pairwise relative frequency scores
                for i in range(n - 1):
                    resultDict[ID][1] += relFreq[(text[i], text[i+1])]
            else:
                resultDict[ID] = [originalTweets[ID], -1]
        except Exception as e:
            print(str(e) + '\n' + ID + '\n' + text)

    return resultDict

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

with open(pairwiseRankAllTweetsTextResultsFile, 'w') as f:
    f.write(textAllResults)

with open(pairwiseRankAllTweetsDictFile, 'wb') as f:
    pickle.dump(allTweetRank, f)

with open(pairwiseRankAllTweetsListFile, 'wb') as f:
    pickle.dump(allSortedByValue, f)

with open(pairwiseRankUnambiguousTweetsTextResultsFile, 'w') as f:
    f.write(textUnambiguousResults)

with open(pairwiseRankUnambiguousTweetsDictFile, 'wb') as f:
    pickle.dump(unambiguousTweetRank, f)

with open(pairwiseRankUnambiguousTweetsListFile, 'wb') as f:
    pickle.dump(unambiguousSortedByValue, f)

with open(pairwiseRankAmbiguousTweetsTextResultsFile, 'w') as f:
    f.write(textAmbiguousResults)

with open(pairwiseRankAmbiguousTweetsDictFile, 'wb') as f:
    pickle.dump(ambiguousTweetRank, f)

with open(pairwiseRankAmbiguousTweetsListFile, 'wb') as f:
    pickle.dump(ambiguousSortedByValue, f)
