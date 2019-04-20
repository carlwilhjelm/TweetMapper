# DEPRECATED
# from LocalDir import *
# import pickle
#
# listSizes = []
# with open(trainingDataSizesTextFile, 'r') as f:
#     for line in f.readlines():
#         valKey = line.split(",")
#         val = int(valKey[0][1:])
#         key = str(valKey[1][2:-3])
#         listSizes.append((val, key))
#
# with open(trainingDataSizesListFile, 'wb') as f:
#     pickle.dump(listSizes, f)
#
# with open(allWordsListFile, 'rb') as f:
#     allWordsList = pickle.load(f)
#
# sortedPredictionsByWordDict = {}
# for word in allWordsList:
#     with open(nbTrainingDir + word + "SortedPredictions.ListObj", 'rb') as f:
#         sortedPredictionsByWordDict[word] = pickle.load(f)
#
# with open(sortedPredictionsListsByWordFile, 'wb') as f:
#     pickle.dump(sortedPredictionsByWordDict, f)