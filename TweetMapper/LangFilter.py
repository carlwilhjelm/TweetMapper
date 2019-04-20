# takes tweet ID based dictionary and filters out english only tweets
# outputs dictionary of ID's and text only
import json
from LocalDir import *
from langdetect import detect
import pickle

with open(rawTweetByIdDictFile, 'rb') as f:
    tweetDict = pickle.load(f)

englishOnlyTweets = {}
total = 0
englishOnlyTotal = 0
foreignLanguageTotal = 0
failedTotal = 0

for ID, fullTweet in tweetDict.items():
    tweet = json.loads(fullTweet)
    if tweet['lang'] != 'en':
        foreignLanguageTotal += 1
        continue
    try:
        text = tweet['extended_tweet']['full_text']
    except:
        text = tweet['text']
    total += 1
    try:
        if detect(text) == 'en':
            englishOnlyTweets[ID] = text
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

with open(allEnglishTweetsByIdDictFile, 'wb') as f:
    pickle.dump(englishOnlyTweets, f)
