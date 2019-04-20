# takes dictionary of tweets by word, as sorted by TweetBayesModel
# allows user to create labels 1 for does have to do with drugs 0 for not
# user must set wordForTraining to draw unlabeled data from
from LocalDir import *
import pickle
import textwrap

wordForTraining = "addiction"

# take set of unlabeled tweets for this word from the dictionary object created in BayesByWordDictRankSet.py
with open(sortedPredictionsSetsByWordFile, 'rb') as f:
    tweetSetsByWord = pickle.load(f)
    unlabeledTweetSet = tweetSetsByWord[wordForTraining]

# load set of original tweets to print when cleaned and lemmatized version is unclear in meaning
with open(allEnglishTweetsByIdDictFile, 'rb') as f:
    originalTweets = pickle.load(f)

# load and store a list of all tweets labeled from this program to be more easily appended to other training data
try:
    with open(labeledWordDictSetListFile, 'rb') as f:
        oldLabelList = pickle.load(f)
except FileNotFoundError:
    oldLabelList = []

# load the dictionary of tweets by word
try:
    with open(labeledWordDictSetByWordFile, 'rb') as f:
        labelListByWord = pickle.load(f)
except FileNotFoundError:
    print("no prior dictionary of labels / error loading previous labels")
    labelListByWord = {}

# assign variable for set of tweets consistent with wordForTraining
try:
    labelListForTrainingWord = labelListByWord[wordForTraining]
    print("Total Labels: " + str(len(labelListForTrainingWord)))
except KeyError:
    print("no prior labels for this word / error loading previous set")
    labelListForTrainingWord = []

# load counts of labeled tweets by word
try:
    with open(labelCountWordDictFile, 'rb') as f:
        totalIndexByWord = pickle.load(f)
except FileNotFoundError:
    print("no prior count dictionary/ error loading previous counts")
    totalIndexByWord = {}

# assign count for this wordForTraining
try:
    totalIndex = totalIndexByWord[wordForTraining]
    print('Total Index for ' + wordForTraining + ": " + str(totalIndex))
except KeyError:
    print("no prior count / error loading previous count")
    totalIndex = 0

# load skipped of labeled tweets by word
try:
    with open(labelSkippedWordDictFile, 'rb') as f:
        skippedByWord = pickle.load(f)
except FileNotFoundError:
    print("no prior skipped dictionary/ error loading previous skipped by word")
    skippedByWord = {}

# assign skipped for this wordForTraining
try:
    skipped = skippedByWord[wordForTraining]
    print("Skipped: " + str(skipped))
except KeyError:
    skipped = []
    print("no prior skipped / error loading previous skipped")

prompt = 'label must be 1, 0, 9 to back, 7 to skip, 5 to see original text, ' \
         '\n 321 to save and exit, or 999 to reset all saves \n'

print(prompt)
textResults = ""

i = totalIndex
reset = False
if i >= len(unlabeledTweetSet):
    print("All tweets for this word have previously been labeled")

newLabelList = []
# as long as there are unlabeled or skipped tweets for this word
# get user to label the word
while i < len(unlabeledTweetSet):
    ID = unlabeledTweetSet[i][2]
    tokens = unlabeledTweetSet[i][1]
    score = unlabeledTweetSet[i][0]
    print(score)
    text = " ".join(tokens)
    label = input(textwrap.fill(text, width=150, drop_whitespace=False))
    if label == '1' or label == '0':
        print('label = ' + str(label) + '\n')
        labelListForTrainingWord.append([label, tokens, ID])
        newLabelList.append([label, tokens, ID])
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
                labelListForTrainingWord.pop(i - len(skipped))
            else:
                skipped.remove(i)
    elif label == '321':
        break
    elif label == '999':
        print('Are you sure you want to delete all saved progress?')
        conf = input("retype \'999\' to confirm")
        if conf == '999':
            labelListByWord = {}
            skippedByWord = {}
            totalIndexByWord = {}
            newLabelList = []
            reset = True
            break
    else:
        print(prompt)

if not reset:
    # update index variable to be saved
    totalIndexByWord[wordForTraining] = i
    # assign updated list to dictionary and print all labels for debugging
    labelListByWord[wordForTraining] = labelListForTrainingWord
    for line in labelListForTrainingWord:
        print(line)
    print("Skipped: " + str(skipped))
    skippedByWord[wordForTraining] = skipped
    print("Total labels for " + wordForTraining + ": " + str(len(labelListForTrainingWord)))
    newLabelList = oldLabelList + newLabelList
    print("Total labels = " + str(len(newLabelList)))

# appends results to previous results in text and list obj
with open(labeledWordDictSetTextResultsFile, 'a') as f:
    f.write(textResults)

with open(labeledWordDictSetByWordFile, 'wb') as f:
    pickle.dump(labelListByWord, f)

with open(labeledWordDictSetListFile, 'wb') as f:
    pickle.dump(newLabelList, f)

# maintains total index so progress can be saved and continued
with open(labelCountWordDictFile, 'wb') as f:
    pickle.dump(totalIndexByWord, f)

# maintains skipped list so progress can be saved and continued
with open(labelSkippedWordDictFile, 'wb') as f:
    pickle.dump(skippedByWord, f)
