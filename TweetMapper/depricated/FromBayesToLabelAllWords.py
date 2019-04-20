# DEPRECATED
# # take dictionaries of words from TrainingDataFromBayesPart1 and create a super list pulling from top and bottom
# # of each dictionary incrementally to create a new list of training data from the naive bayes
# from LocalDir import *
# from collections import defaultdict
# import pickle
#
# with open(trainingDataSizesListFile, 'rb') as f:
#     listSizesByWord = pickle.load(f)
#
# with open(sortedPredictionsListsByWordFile, 'rb') as f:
#     sortedPredictionsByWordDict = pickle.load(f)
#
# with open(allWordsListFile, 'rb') as f:
#     allWordsList = pickle.load(f)
#
# totalNumberOfTweetsToTrain = 1000
# uniqueTweetsToTrain = defaultdict(int)
# i = 0
# # if we have enough tweets break
# while len(uniqueTweetsToTrain) < totalNumberOfTweetsToTrain:
#     # if the size of the list associated with the key is less than i/2 remove it
#     for key in allWordsList:
#         list = sortedPredictionsByWordDict[key]
#         if abs(i) >= len(list)/2:
#             allWordsList.remove(key)
#         else:
#             tweet = " ".join(list[i])
#             # no duplicates
#             if not tweet in uniqueTweetsToTrain:
#                 uniqueTweetsToTrain[tweet]
#     # approach middle of each list from outside s.t. take the most and least likely tweets to be about drugs evenly
#     i = (i*-1-1, i*-1)[i < 0]
#     if len(allWordsList) < 1:
#         break
#
# tweetsToTrainList = []
# for tweet, val in uniqueTweetsToTrain.items():
#     tweetsToTrainList.append(tweet)
#
# with open(trainingDataFromBayesToLabelFile, 'wb') as f:
#     pickle.dump(tweetsToTrainList, f)
#
