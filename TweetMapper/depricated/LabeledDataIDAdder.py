# # DEPRECATED
# # takes original list from version 0.8 with labels but no IDs and appends labels in order
# # to data from re-worked TweetRankSet version 0.8b that includes IDs in list form [ID, text]
# # final data will be output in format [label, ID, text], where text comes from version 0.9
#
# from LocalDir import *
# import pickle
#
# # version 0.8 LabeledAmbiguousTweetSet.ListObj, with no IDs
# with open(labeledAmbiguousTweetSetListFile) as f:
#     v8Labels_noIDs = pickle.load(f)
#
# with open(labelSkippedFile, 'rb') as f:
#     skipped = pickle.load(f)
#
# # open the old count file
# with open(labelCountFile, 'rb') as f:
#     total = pickle.load(f)
#
# # version 0.8b TweetRankSet with IDs
# with open(pairwiseRankSetAmbiguousTweetsListFile) as f:
#     v8bSet = pickle.load(f)
#
# # version 0.9 allTweetsTokenized, for text
# with open(allTokenizedTweetsDictFile, 'rb') as f:
#     allTweetsTokenized = pickle.load(f)
#
#
# # iterate through the total number of tweets, if the ID did not make it through the new mapper
# # or if the number belongs to the skipped tweets, skip
# results = []
# labelIndex = 0
# for i in range(total):
#     if i in skipped:
#         continue
#     label = v8Labels_noIDs[labelIndex][0]
#     labelIndex += 1
#     ID = v8bSet[i][0]
#     try:
#         text = allTweetsTokenized[ID]
#     except KeyError:
#         False
#     results.append([label, text, ID])
#
# print(len(results))
#
# with open(labeledAmbiguousTweetSetListFile_v8b) as f:
#     pickle.dump(results, f)
#
