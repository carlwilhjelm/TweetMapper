# takes tweet ID based dictionary and filters out english only tweets
from LocalDir import *
from langdetect import detect
import pickle
import re

# regex to find tweet text
textRegex = re.compile('(?<="text":").*?(?=",")')

with open(rawTweetByIdDictFile, 'rb') as f:
    tweetDict = pickle.load(f)

englishOnlyTweets = {}
total = 0
englishOnlyTotal = 0
foreignLanguageTotal = 0
failedTotal = 0

for ID, fullTweet in tweetDict.items():
    tweet = textRegex.search(fullTweet).group()
    total += 1
    try:
        if detect(tweet) == 'en':
            englishOnlyTweets[ID] = fullTweet
            englishOnlyTotal += 1
        else:
            foreignLanguageTotal += 1
    except:
        failedTotal += 1

results = "Total tweets = " + str(total) + \
          "\nEnglish only tweets = " + str(englishOnlyTotal) + \
          "\nForeign language tweets = " + str(foreignLanguageTotal) + \
          "\nTotal langdetect failures = " + str(failedTotal)

with open(langFilterTextResultsFile, 'w') as f:
    f.write(results)

with open(tweetByIdDictFile, 'wb') as f:
    pickle.dump(englishOnlyTweets, f)
