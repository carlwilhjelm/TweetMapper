from LocalDir import *
import pickle

# load tokenized tweets
with open(allTokenizedTweetsDictFile, 'rb') as f:
    allTweetsTokenized = pickle.load(f)

with open(unambiguousTokenizedTweetsDictFile, 'rb') as f:
    unambiguousTokenizedTweets = pickle.load(f)

with open(ambiguousTokenizedTweetsDictFile, 'rb') as f:
    ambiguousTokenizedTweets = pickle.load(f)

# load relative frequency dictionary
with open(pairwiseRelFreqDictFile, 'rb') as f:
    relFreq = pickle.load(f)

textAllResults = ""
textUnambiguousResults = ""
textAmbiguousResults = ""
allTweetRank = {}
unambiguousTweetRank = {}
ambiguousTweetRank = {}

# rank tweets from @param loaded tweet by ID dictionary object
# returns dictionary[ID] = (tokens, score)
def setRank(tweetSetIn):
    resultDict = {}
    for ID, text in tweetSetIn.items():
        n = len(text)
        # if tweet has a length of 1 or fewer assign score of -1
        try:
            if n > 1:
                resultDict[ID] = [allTweetsTokenized[ID], 0]
                # rank equals sum of pairwise relative frequency scores
                for i in range(n - 1):
                    resultDict[ID][1] += relFreq[(text[i], text[i+1])]
            else:
                resultDict[ID] = [allTweetsTokenized[ID], -1]
        except Exception as e:
            print(str(e) + '\n' + ID + '\n' + text)

    return resultDict

unambiguousTweetRank = setRank(unambiguousTokenizedTweets)
ambiguousTweetRank = setRank(ambiguousTokenizedTweets)
allTweetRank = unambiguousTweetRank.copy()
allTweetRank.update(ambiguousTweetRank)

allTweetRankList = [[tokenScore[1], tokenScore[0], ID] for ID, tokenScore in allTweetRank.items()]
allSortedByValue = sorted(allTweetRankList, key=lambda kv: kv[0])
for score, tokens, ID in allSortedByValue:
    textAllResults += str(score) + ": " + " ".join(tokens) + ID + '\n'

unambiguousTweetRankList = [[tokenScore[1], tokenScore[0], ID] for ID, tokenScore in unambiguousTweetRank.items()]
unambiguousSortedByValue = sorted(unambiguousTweetRankList, key=lambda kv: kv[0])
for score, tokens, ID in unambiguousSortedByValue:
    textUnambiguousResults += str(score) + ": " + " ".join(tokens) + ID + '\n'

ambiguousTweetRankList = [[tokenScore[1], tokenScore[0], ID] for ID, tokenScore in ambiguousTweetRank.items()]
ambiguousSortedByValue = sorted(ambiguousTweetRankList, key=lambda kv: kv[0])
for score, tokens, ID in ambiguousSortedByValue:
    textAmbiguousResults += str(score) + ": " + " ".join(tokens) + ID + '\n'

with open(pairwiseRankAllTweetsTextResultsFile, 'w', encoding='utf16') as f:
    f.write(textAllResults)

with open(pairwiseRankAllTweetsDictFile, 'wb') as f:
    pickle.dump(allTweetRank, f)

with open(pairwiseRankAllTweetsListFile, 'wb') as f:
    pickle.dump(allSortedByValue, f)

with open(pairwiseRankUnambiguousTweetsTextResultsFile, 'w', encoding='utf16') as f:
    f.write(textUnambiguousResults)

with open(pairwiseRankUnambiguousTweetsDictFile, 'wb') as f:
    pickle.dump(unambiguousTweetRank, f)

with open(pairwiseRankUnambiguousTweetsListFile, 'wb') as f:
    pickle.dump(unambiguousSortedByValue, f)

with open(pairwiseRankAmbiguousTweetsTextResultsFile, 'w', encoding='utf16') as f:
    f.write(textAmbiguousResults)

with open(pairwiseRankAmbiguousTweetsDictFile, 'wb') as f:
    pickle.dump(ambiguousTweetRank, f)

with open(pairwiseRankAmbiguousTweetsListFile, 'wb') as f:
    pickle.dump(ambiguousSortedByValue, f)
