# takes set of ambiguous tweets and alows user to create labels
# 1 for does have to do with drugs 0 for not
from LocalDir import *
import pickle
import textwrap

# takes list file of tweet text
with open(pairwiseRankSetAmbiguousTweetsListFile, 'rb') as f:
    tweetSet = pickle.load(f)

with open(allEnglishTweetsByIdDictFile, 'rb') as f:
    originalTweets = pickle.load(f)

try:
    with open(labeledAmbiguousTweetSetListFile, 'rb') as f:
        labelList = pickle.load(f)
        print("Total Labels: " + str(len(labelList)))

except:
    print("no prior labels / error loading previous set")
    labelList = []

try:
    with open(labelCountFile, 'rb') as f:
        totalIndex = pickle.load(f)
        print('Total Index: ' + str(totalIndex))
except:
    print("no prior count / error loading previous count")
    totalIndex = 0

try:
    with open(labelSkippedFile, 'rb') as f:
        skipped = pickle.load(f)
        print("Skipped: " + str(skipped))
except:
    skipped = []
    print("no prior skipped / error loading previous skipped")

prompt = 'label must be 1, 0, 9 to back, 7 to skip, 5 to see original text, ' \
         '\n 321 to save and exit, or 999 to reset all saves \n'

print(prompt)
textResults = ""

i = totalIndex

while i < len(tweetSet):
    ID = tweetSet[i][0]
    tokens = tweetSet[i][1][0]
    text = " ".join(tokens)
    label = input(textwrap.fill(text, width=150, drop_whitespace=False))
    if label == '1' or label == '0':
        print('label = ' + str(label) + '\n')
        labelList.append([label, tokens, ID])
        textResults += str(label) + ": " + text + '\n'
        i += 1
    elif label == '5':
        print('expanded tweet:')
        print(textwrap.fill(originalTweets[ID], width=150, drop_whitespace=False), end='\n\n')
    elif label == '7':
        print("Skipped\n")
        skipped.append(i)
        i += 1
    elif label == '9':
        if i <= totalIndex:
            print("currently on 0th tweet\n")
        else:
            print("returning to previous tweet\n")
            i -= 1
            if i not in skipped:
                labelList.pop(i-len(skipped))
            else:
                skipped.remove(i)
    elif label == '321':
        break
    elif label == '999':
        print('Are you sure you want to delete all saved progress?')
        conf = input("retype \'999\' to confirm")
        if conf == '999':
            labelList = []
            totalIndex = 0
            i = totalIndex
            continue
    else:
        print(prompt)

# reset index variable to be saved
totalIndex = i

# print all labels for debugging
for line in labelList:
    print(line)

print("Skipped: " + str(skipped))

# appends results to previous results in text and list obj
with open(labeledAmbiguousTweetSetTextResultsFile, 'a') as f:
    f.write(textResults)

with open(labeledAmbiguousTweetSetListFile, 'wb') as f:
    pickle.dump(labelList, f)

# maintains total index so progress can be saved and continued
with open(labelCountFile, 'wb') as f:
    pickle.dump(totalIndex, f)

# maintains skipped list so progress can be saved and continued
with open(labelSkippedFile, 'wb') as f:
    pickle.dump(skipped, f)
