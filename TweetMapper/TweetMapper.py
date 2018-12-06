# partitions ID dictionary of tweets based on whether or not they contain unambiguous words
# creates dictionaries of ID and tokenized spell checked text only
from autocorrect import spell
from LocalDir import *
from collections import defaultdict
import nltk
from nltk import word_tokenize as tok
import re
import pickle

# nltk lematizer
wnl = nltk.WordNetLemmatizer()

# regex to find if retweet
rtRegex = re.compile('("text":"RT @)')
# regex to find tweet text
textRegex = re.compile('(?<="text":").*?(?=",")')
# regex to find truncated status of tweet
truncatedRegex = re.compile('(?<="truncated":).*?(?=,")')
# regex to find tweet full text
fullTextRegex = re.compile('(?<="full_text":").*?(?=",")')

# load unambiguous dictionary
with open(unambiguousWordsListFile, "rb") as f:
    unambiguousDictionary = pickle.load(f)

# load ID dictionary of tweets
with open(tweetByIdDictFile, 'rb') as f:
    allTweetsIDDict = pickle.load(f)

invertedIndexCount = defaultdict(int)
allTweetsText = {}
allTweetsTokenized = {}
ambiguousTweets = {}
unambiguousTweets = {}
unambiguousHits = 0
textResults = ""

for ID, tweet in allTweetsIDDict.items():
    try:
        tweetText = fullTextRegex.search(tweet).group()
    except:
        tweetText = textRegex.search(tweet).group()

    allTweetsText[ID] = tweetText

    textList = list(tweetText)
    for i in range(len(textList)):
        if not textList[i].isalpha():
            textList[i] = " "

    tweetText = tok("".join(textList))
    for i in range(len(tweetText)):
        # s = spell(tweetText[i])
        s = tweetText[i]
        tweetText[i] = wnl.lemmatize(s).lower()

    # check for tweets that have no characters for some reason
    if len(tweetText) == 0:
        continue
    containsUnambiguous = False
    for elem in unambiguousDictionary:
        if elem in tweetText:
                invertedIndexCount[elem] += 1
                unambiguousHits += 1
                containsUnambiguous = True
                break
    if containsUnambiguous:
        unambiguousTweets[ID] = tweetText
    else:
        ambiguousTweets[ID] = tweetText
    allTweetsTokenized[ID] = tweetText

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

with open(textByIdDictFile, 'wb') as f:
    pickle.dump(allTweetsText, f)

