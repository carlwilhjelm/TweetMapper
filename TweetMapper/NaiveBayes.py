# create a naive bayes model to sort tweets by likelihood of their being about drugs
from LocalDir import *
from collections import defaultdict
import pickle
import numpy as np

# N GRAM: sum total instances of relevant words in tweet
# @param trainingSet in is array of tokenized and cleaned tweets
# @return the word dict with weights corresponding to instances and the total count of words NOT including duplicates
def wordSum(trainingSetIn):
    wordDict = defaultdict(int)
    nOut = 0
    for tokens in trainingSetIn:
        for i in range(len(tokens)):
            wordDict[tokens[i]] += 1
            #total number of words in this set
            nOut += 1
    return wordDict, nOut

# N GRAM: sum total instances of relevant words in tweet
# @param trainingSet in is array of tokenized and cleaned tweets
# @return the word dict with weights corresponding to instances and the total count of words NOT including duplicates
def wordSumNGram(trainingSetIn, nGramSizeIn):
    wordDict = defaultdict(int)
    nOut = 0
    for tokens in trainingSetIn:
        for i in range(len(tokens) + 1 - nGramSizeIn):
            nGram = " ".join(tokens[i:i + nGramSizeIn])
            wordDict[nGram] += 1
            #total number of words in this set
            nOut += 1
    return wordDict, nOut

# return numpy array of all boolean labels, with list of all tweets assigned 1
# @param totalNeg represents total tweets of false label in test set
# @param totalPos represents total tweets of true label in test set
def predictBool(falseWordDictIn, trueWordDictIn, testSetIn, totalPosIn, totalNegIn, sumTotalIn):
    predictionsWithCertainty = []
    # for each list of tokens in the testSetIn
    for score, tokens, ID in testSetIn:
        # initialize probabilities to 1
        negProb = 1
        posProb = 1
        # for every nGram
        for i in range(len(tokens)):
            # normalize totals for words that have not previously been recorded in either set
            alpha = 1
            sumOfFalseInTraining = falseWordDictIn[tokens[i]]
            sumOfTrueInTraining = trueWordDictIn[tokens[i]]
            # negProb is probability that the model will label the tweet false
            negProb *= (alpha + sumOfFalseInTraining) / (totalNegIn + alpha * sumTotalIn)
            posProb *= (alpha + sumOfTrueInTraining) / (totalPosIn + alpha * sumTotalIn)
        score = 1 if posProb - negProb >= 0 else 0
        predictionsWithCertainty.append((score, tokens, ID))

    # return all tweets with positive predictions
    posPred = [line for line in predictionsWithCertainty if line[0] == 1]
    pred = [str(score) for score, tokens, ID, in predictionsWithCertainty]
    pred = np.array(pred)

    return pred, posPred

# return total number of positive and negative tweets predicted in each set
# @param totalNeg represents total tweets of opposite label as test set
# @param totalPos representd total tweets of same label as test set
def predictScore(falseWordDictIn, trueWordDictIn, testSetIn, totalPosIn, totalNegIn, sumTotalIn):
    predictionsWithCertainty = []
    # for each list of tokens in the testSetIn
    for tokens, ID in testSetIn:
        # initialize probabilities to 1
        negProb = 1
        posProb = 1
        # for every nGram
        # print(tokens)
        for i in range(len(tokens)):
            # normalize totals for words that have not previously been recorded in either set
            alpha = 1
            sumOfFalseInTraining = falseWordDictIn[tokens[i]]
            sumOfTrueInTraining = trueWordDictIn[tokens[i]]
            # negProb is probability that the model will label the tweet false
            negProb *= (alpha + sumOfFalseInTraining) / (totalNegIn + alpha * sumTotalIn)
            posProb *= (alpha + sumOfTrueInTraining) / (totalPosIn + alpha * sumTotalIn)
        predictionsWithCertainty.append((posProb - negProb, tokens, ID))
    predictionsWithCertainty.sort(key=lambda x: x[0])
    return predictionsWithCertainty

# return total number of positive and negative tweets predicted in each set
# @param totalNeg represents total tweets of opposite label as test set
# @param totalPos representd total tweets of same label as test set
def predictNGramsScore(falseWordDictIn, trueWordDictIn, testSetIn, totalPosIn, totalNegIn, sumTotalIn, nGramSizeIn):
    predictionsWithCertainty = []
    # for each list of tokens in the testSetIn
    for tokens, ID in testSetIn:
        # initialize probabilities to 1
        negProb = 1
        posProb = 1
        # for every nGram
        for i in range(len(tokens) + 1 - nGramSizeIn):
            nGram = " ".join(tokens[i:i + nGramSizeIn])
            # normalize totals for words that have not previously been recorded in either set
            alpha = 1
            sumOfFalseInTraining = falseWordDictIn[nGram]
            sumOfTrueInTraining = trueWordDictIn[nGram]
            # negProb is probability that the model will label the tweet incorrectly
            negProb *= (alpha + sumOfFalseInTraining) / (totalNegIn + alpha * sumTotalIn)
            posProb *= (alpha + sumOfTrueInTraining) / (totalPosIn + alpha * sumTotalIn)
        predictionsWithCertainty.append((posProb - negProb, tokens, ID))
    predictionsWithCertainty.sort(key=lambda x: x[0])
    return predictionsWithCertainty


def naiveBayes(wordIn):

    # load training data format [label, tokens, ID]
    with open(labeledTweetsFile, 'rb') as f:
        trainingData = pickle.load(f)

    # load testing data format [pairwiseRank, tokens, ID]
    # rank will be ignored for all computations only considered for code reusability
    with open(sortedPredictionsSetsByWordFile, 'rb') as f:
        wordDictRankSet = pickle.load(f)

    #  only using results for tweets containing...
    testSet = wordDictRankSet[wordIn]

    # # set n for ngrams
    # nGramSize = 1

    # separate list into affirmative and negative
    trueImplicit = []
    falseImplicit = []
    for label, tokens, ID in trainingData:
        if label == '1':
            trueImplicit.append(tokens)
        else:
            falseImplicit.append(tokens)

    # create default dictionaries of sums of each word from each training set
    falseWordDict, totalFalse = wordSum(falseImplicit)
    trueWordDict, totalTrue = wordSum(trueImplicit)
    sumTotal = len(falseWordDict) + len(trueWordDict)
    boolPredictions = predictBool(falseWordDict, trueWordDict, testSet, totalTrue, totalFalse, sumTotal)

    return boolPredictions



#
# testResult = ""
# for i in range(len(sortedPredictions)):
#     testResult += str(sortedPredictions[i]) + "\n"
#
# with open(sortedBayesPredictionsTextResultsFile, 'w') as f:
#     f.write(testResult)
#
# with open(sortedBayesPredictionsListFile, 'wb') as f:
#     pickle.dump(sortedPredictions, f)
