# partitions ID dictionary of tweets based on whether or not they contain unambiguous words
# creates dictionaries of ID and cleaned tokenized text
from LocalDir import *
from collections import defaultdict
import pickle
from TweetToTokens import tweetToTokens

# load unambiguous dictionary
with open(unambiguousWordsListFile, "rb") as f:
    unambiguousDictionary = pickle.load(f)

# load ID dictionary of tweets
with open(allEnglishTweetsByIdDictFile, 'rb') as f:
    allTweetsIDDict = pickle.load(f)

invertedIndexCount = defaultdict(int)
allTweetsTokenized = {}
ambiguousTweets = {}
unambiguousTweets = {}
unambiguousHits = 0
textResults = ""

for ID, text in allTweetsIDDict.items():
    containsUnambiguous = False
    text = text.lower()
    for elem in unambiguousDictionary:
        if elem in text:
                invertedIndexCount[elem] += 1
                unambiguousHits += 1
                containsUnambiguous = True
    cleanText = tweetToTokens(text)
    if containsUnambiguous:
        unambiguousTweets[ID] = cleanText
    else:
        ambiguousTweets[ID] = cleanText
    allTweetsTokenized[ID] = cleanText

textResults += "Total tweets: " + str(len(ambiguousTweets)) \
               + "\nTotal unambiguous tweets: " + str(len(unambiguousTweets)) \
                + "\nTotal unambiguous hits: " + str(unambiguousHits)

with open(mapperTextResultsFile, 'w') as f:
    f.write(textResults)

with open(unambiguousTokenizedTweetsDictFile, 'wb') as f:
    pickle.dump(unambiguousTweets, f)

with open(ambiguousTokenizedTweetsDictFile, 'wb') as f:
    pickle.dump(ambiguousTweets, f)

with open(allTokenizedTweetsDictFile, 'wb') as f:
    pickle.dump(allTweetsTokenized, f)

