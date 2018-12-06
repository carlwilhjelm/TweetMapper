from LocalDir import *
import carmen
import json
import re

# tweet file
tweetFile = sourceDir + "tweetStream.2018.09.17.json"
# object file for storing dict for location by tweet id
allTweetsLocFile = localDir + "LocByIDDictObj.txt"

# regex for finding location
locRegex = re.compile('(?<="location":).*?(?=,")')
resolver = carmen.get_resolver()
resolver.load_locations()
with open(tweetFile, 'r') as f:
    allTweets = f.readlines()

for line in allTweets:
    tweet = json.loads(line)
    loc = locRegex.search(line)[0]
    locPrime = resolver.resolve_tweet(tweet)
    print(loc + ": " + str(locPrime))