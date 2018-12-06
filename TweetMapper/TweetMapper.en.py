from collections import defaultdict
import re
import pickle
from os import listdir
from os.path import isfile, join

#regex to find tweet ID
idRegex = re.compile('(?<="id_str":").*?(?=",")')
# regex to find tweet text
textRegex = re.compile('(?<="text":").*?(?=",")')
# directory for json files as input
langRegex = re.compile('(?<="lang":").*?(?=",")')
# directory for json files as input
sourceDir = "D:\School\GSU\Skums\\tweets\APIStream.2018.09.17"
# directory for output files
destDir = sourceDir + "\\results\\"
# directory for dictionary file made with pickle module
dictFile = "D:\School\GSU\Skums\dictionary\metaDictUnambiguousObj.txt"
# where text of results is stored
outTextResultsFile = destDir + "MapResults.en.txt"
# where all tweets results obj is stored
outAllTweetsFile = destDir + "AllTweetsObj.en.txt"
# where unambiguous tweets results obj is stored
outUnambiguousTweetsFile = destDir + "UnambiguousTweetsObj.en.txt"
# list of json files, in case of folders with multiple files
onlyFiles = [f for f in listdir(sourceDir) if isfile(join(sourceDir, f))]
print(onlyFiles)

with open(dictFile, "rb") as f:
    dictionary = pickle.load(f)

invertedIndexCount = defaultdict(int)
allTweets = []
unambiguousTweets = []
unambiguousHits = 0
textResults = ""

for file in onlyFiles:
    with open(sourceDir + "\\\\" + file) as jsonFile:
        for tweet in jsonFile:
            tweetText = textRegex.search(tweet)[0]
            tweetID = idRegex.search(tweet)[0]
            langID = langRegex.search(tweet)[0]
            if langID != 'en':
                continue
            print(tweetText)
            containsUnambiguous = False
            for elem in dictionary:
                if elem in tweetText:
                    invertedIndexCount[elem] += 1
                    unambiguousHits += 1
                    containsUnambiguous = True
            if containsUnambiguous:
                unambiguousTweets.append((tweetID, tweetText))
            allTweets.append((tweetID, tweetText))

textResults += "Total tweets: " + str(len(allTweets)) \
               + "\nTotal unambiguous tweets: " + str(len(unambiguousTweets)) \
                + "\nTotal unambiguous hits: " + str(unambiguousHits)

with open(outTextResultsFile, 'w') as f:
    f.write(textResults)

with open(outUnambiguousTweetsFile, 'wb') as f:
    pickle.dump(unambiguousTweets, f)

with open(outAllTweetsFile, 'wb') as f:
    pickle.dump(allTweets, f)

