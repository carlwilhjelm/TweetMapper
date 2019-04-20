from LocalDir import *
import pickle
import carmen
import json
import re
from collections import defaultdict

countryRe = re.compile("(?<=country=').*?(?=')")
stateRe = re.compile("(?<=state=').*?(?=')")

with open(word2VecSVMPosLabelsByIDFile, 'rb') as f:
    labelsById = pickle.load(f)

with open(rawTweetByIdDictFile, 'rb') as f:
    rawTweetsDict = pickle.load(f)

resolver = carmen.get_resolver()
resolver.load_locations()

total = 0
hasCoord = 0
allCountries = defaultdict(int)
allStates = defaultdict(int)
for ID in labelsById:
    total += 1
    tweet = json.loads(rawTweetsDict[ID])
    locReso = resolver.resolve_tweet(tweet)
    locOrig = tweet['user']['location']
    coordinates = tweet['coordinates']
    print(str(locOrig) + ": " + str(locReso))
    if coordinates is not None:
        hasCoord += 1
        print(coordinates)
    if locReso is not None:
        location = str(locReso)
        country = countryRe.search(location).group()
        allCountries[country] += 1
        state = stateRe.search(location)
        if country == 'United States' and state is not None:
            allStates[state.group()] += 1

textResults = "Total = " + str(total)
textResults += "\nHas coordinates = " + str(hasCoord)

textResults += "\nCountries"
for line in allCountries.items():
    textResults += '\n\t' + str(line)

allStatesList = sorted(allStates.items(), key=lambda kv: kv[1], reverse=True)

textResults += "\nStates"
for line in allStatesList:
    textResults += '\n\t' + str(line)

with open(identifiedTweetLocResultsFile, 'w') as f:
    f.write(textResults)