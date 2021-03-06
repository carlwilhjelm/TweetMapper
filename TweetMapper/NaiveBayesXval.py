from LocalDir import *
from collections import defaultdict
import pickle
import random
from TweetToTokens import tweetToTokens

# take labeled tweets made from LabelMakerFromPairwise.py of the form ["label", "text"]
with open(labeledTweetsFile, 'rb') as f:
    labeledTweets = pickle.load(f)

# partition lists of tweets into training and testing
def trainTestPartition(listIn):
    n = len(listIn)
    m = 5
    random.shuffle(listIn)
    train = listIn[:-(n//m)]
    test = listIn[-(n//m):]
    return train, test

# N GRAM: sum total instances of relevant words in tweet
# @param trainingSet in is array of tokenized and cleaned tweets
# @return the word dict with weights corresponding to instances and the total count of words NOT including duplicates
def wordSumNGram(trainingSetIn, nGramSizeIn):
    wordDict = defaultdict(int)
    nOut = 0
    for tokens in trainingSetIn:
        for i in range(len(tokens) + 1 - nGramSizeIn):
            nGram = " ".join(tokens[i:i+nGramSizeIn])
            wordDict[nGram] += 1
            #total number of words in this set
            nOut += 1
        # # total number of tweets in this set
        # nOut += 1
    return wordDict, nOut

# return total number of positive and negative tweets predicted in each set
# @param totalNeg represents total tweets of opposite label as test set
# @param totalPos representd total tweets of same label as test set
def predict(negWordDictIn, posWordDictIn, testSetIn, totalPosIn, totalNegIn, sumTotalIn, nGramSizeIn):
    wrong = 0
    correct = 0
    predictionsWithCertainty = []
    # for each list of tokens in the testSetIn
    for tokens in testSetIn:
        # initialize probabilities to 1
        negProb = 1
        posProb = 1
        # for every nGram
        for i in range(len(tokens) + 1 - nGramSizeIn):
            nGram = " ".join(tokens[i:i+nGramSizeIn])
            # normalize totals for words that have not previously been recorded in either set
            negTotal = negWordDictIn[nGram]
            posTotal = posWordDictIn[nGram]
            # negProb is probability that the model will label the tweet incorrectly
            alpha = 1
            negProb *= (alpha + negTotal) / (totalNegIn + alpha * sumTotalIn)
            posProb *= (alpha + posTotal) / (totalPosIn + alpha * sumTotalIn)
        if negProb > posProb:
            wrong += 1
            predictionsWithCertainty.append((abs(posProb - negProb), "wrong", tokens))
        else:
            correct += 1
            predictionsWithCertainty.append((abs(posProb - negProb), "correct", tokens))

    predictionsWithCertainty.sort(key=lambda x: x[0], reverse=True)
    return wrong, correct, predictionsWithCertainty

# separate list into affirmative and negative
trueImplicit = []
falseImplicit = []
for label, tokens, ID in labeledTweets:
    if label == '1':
        trueImplicit.append(tokens)
    else:
        falseImplicit.append(tokens)
print("true implicit = " + str(len(trueImplicit)))
print("false implicit = " + str(len(falseImplicit)))

# number of cycles
k = 50
# n for ngrams
nGramSize = 1
# initialize values for calculating accuracy, specificity, and sensitivity
avgAccuracy, lowestAccuracy, highestAccuracy = 0, 1, 0
avgSpecificity, lowestSpecificity, highestSpecificity = 0, 1, 0
avgSensitivity, lowestSensitivity, highestSensitivity = 0, 1, 0

for i in range(k):
    # parse data into separate training and testing sets
    trainTrue, testTrue = trainTestPartition(trueImplicit)
    trainFalse, testFalse = trainTestPartition(falseImplicit)
    # create default dictionaries of sums of each word from each training set
    falseWordDict, totalFalse = wordSumNGram(trainFalse, nGramSize)
    trueWordDict, totalTrue = wordSumNGram(trainTrue, nGramSize)
    sumTotal = len(falseWordDict) + len(trueWordDict)
    # determine number of correct predictions in each set
    falseNeg, trueNeg, sortedPredictions0 = predict(trueWordDict, falseWordDict, testFalse, totalFalse, totalTrue, sumTotal, nGramSize)
    falsePos, truePos, sortedPredictions1 = predict(falseWordDict, trueWordDict, testTrue, totalTrue, totalFalse, sumTotal, nGramSize)

    # calculate accuracy
    correct = (trueNeg + truePos)
    wrong = (falseNeg + falsePos)
    accuracy = correct / (correct + wrong)
    if accuracy < lowestAccuracy: lowestAccuracy = accuracy
    if accuracy > highestAccuracy: highestAccuracy = accuracy
    avgAccuracy += accuracy

    # record sensitivity TP/P and specificity TN/N
    sensitivity = truePos / (truePos + falsePos)
    specificity = trueNeg / (trueNeg + falseNeg)

    # record sensitivity results
    if sensitivity < lowestSensitivity: lowestSensitivity = sensitivity
    if sensitivity > highestSensitivity: highestSensitivity = sensitivity
    avgSensitivity += sensitivity

    # record specificity results
    if specificity < lowestSpecificity: lowestSpecificity = specificity
    if specificity > highestSpecificity: highestSpecificity = specificity
    avgSpecificity += specificity


print("Results for Naive Bayes Model")
print("Results for k = " + str(k) + " iterations")

avgAccuracy = avgAccuracy / k
print("Accuracy:")
print("\thigh = " + str(highestAccuracy))
print("\tavg = " + str(avgAccuracy))
print("\tlow = " + str(lowestAccuracy))

avgSensitivity = avgSensitivity / k
print("Sensitivity:")
print("\thigh = " + str(highestSensitivity))
print("\tavg = " + str(avgSensitivity))
print("\tlow = " + str(lowestSensitivity))

avgSpecificity = avgSpecificity / k
print("Specificity:")
print("\thigh = " + str(highestSpecificity))
print("\tavg = " + str(avgSpecificity))
print("\tlow = " + str(lowestSpecificity))
