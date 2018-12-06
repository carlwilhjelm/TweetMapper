from LocalDir import *
import re
import pickle
from os import listdir
from os.path import isfile, join

# regex to find tweet ID
idRegex = re.compile('(?<="id_str":").*?(?=",")')
# list of json files, in case of folders with multiple files
onlyFiles = [f for f in listdir(sourceDir) if isfile(join(sourceDir, f))]
print(onlyFiles)

allTweets = {}
failedRegex = 0
for file in onlyFiles:
    with open(sourceDir + file, encoding='utf8') as jsonFile:
        for tweet in jsonFile:
            try:
                tweetID = idRegex.search(tweet).group()
                allTweets[tweetID] = tweet
            except:
                failedRegex += 1

print("failed regex: " + str(failedRegex))
with open(rawTweetByIdDictFile, 'wb') as f:
    pickle.dump(allTweets, f)

