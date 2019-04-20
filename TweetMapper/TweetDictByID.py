import json
from LocalDir import *
import pickle
from os import listdir
from os.path import isfile, join

# list of json files, in case of folders with multiple files
onlyFiles = [f for f in listdir(sourceDir) if isfile(join(sourceDir, f))]
print(sourceDir)
print(onlyFiles)

allTweets = {}
failedRegex = 0
for file in onlyFiles:
    with open(sourceDir + file) as jsonFile:
        for line in jsonFile:
            try:
                tweet = json.loads(line, encoding=twitterEncoding)
                tweetID = tweet['id_str']
                allTweets[tweetID] = line
            except:
                failedRegex += 1

print("failed json loads: " + str(failedRegex))
with open(rawTweetByIdDictFile, 'wb') as f:
    pickle.dump(allTweets, f)

