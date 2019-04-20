# maintains directory structure of files
from SuperDir import *

twitterEncoding = 'utf16'

#file path for all words text file
allWordsTextFile = dictDir + "metaDict.txt"
#file path for all words list object
allWordsListFile = dictDir + "metaDict.ListObj"
#file path for unambiguous words text file
unambiguousWordsTextFile = dictDir + "metaDictUnambiguous.txt"
# file path for unambiguous words list obj
unambiguousWordsListFile = dictDir + "metaDictUnambiguous.ListObj"
# where dict of full tweets by id is stored
rawTweetByIdDictFile = localDir + "RawTweetByID.DictObj"
# where text of lang filter results are stored
langFilterTextResultsFile = localDir + "LangFilterResults.txt"
# where full tweets filtered by language dictionary obj is stored
allEnglishTweetsByIdDictFile = localDir + "LangFilteredTweetByID.DictObj"
# where text of mapper results is stored
mapperTextResultsFile = localDir + "Mapping.txt"
# where unambiguous tweets results obj is stored
unambiguousTokenizedTweetsDictFile = localDir + "UnambiguousTokenizedTweets.DictObj"
# where ambiguous tweets results obj is stored
ambiguousTokenizedTweetsDictFile = localDir + "AmbiguousTokenizedTweets.DictObj"
# where tokenized tweets dict obj is stored
allTokenizedTweetsDictFile = localDir + "AllTokenizedTweets.DictObj"

# where text reference of results is stored
pairwiseRelFreqTextResultsFile = pairwiseDir + "PairwiseRelFreq.txt"
# where results sorted list obj is stored
pairwiseRelFreqListFile = pairwiseDir + "PairwiseRelFreq.ListObj"
# where results dict obj is stored
pairwiseRelFreqDictFile = pairwiseDir + "PairwiseRelFreq.DictObj"
# where text of all results is stored
pairwiseRankAllTweetsTextResultsFile = pairwiseDir + "PairwiseRankAllTweets.txt"
# output file for all Tweet Rank dictionary
pairwiseRankAllTweetsDictFile = pairwiseDir + "PairwiseRankAllTweets.DictObj"
# output file for all Tweet Rank list
pairwiseRankAllTweetsListFile = pairwiseDir + "PairwiseRankAllTweets.ListObj"
# where text of unambiguous results is stored
pairwiseRankUnambiguousTweetsTextResultsFile = pairwiseDir + "PairwiseRankUnambiguousTweets.txt"
# output file for unambiguous Tweet Rank dictionary
pairwiseRankUnambiguousTweetsDictFile = pairwiseDir + "PairwiseRankUnambiguousTweets.DictObj"
# output file for unambiguous Tweet Rank list
pairwiseRankUnambiguousTweetsListFile = pairwiseDir + "PairwiseRankUnambiguousTweets.ListObj"
# where text of unambiguous results is stored
pairwiseRankAmbiguousTweetsTextResultsFile = pairwiseDir + "PairwiseRankAmbiguousTweets.txt"
# output file for unambiguous Tweet Rank dictionary
pairwiseRankAmbiguousTweetsDictFile = pairwiseDir + "PairwiseRankAmbiguousTweets.DictObj"
# output file for unambiguous Tweet Rank list
pairwiseRankAmbiguousTweetsListFile = pairwiseDir + "PairwiseRankAmbiguousTweets.ListObj"
# where text of set of ranked ambiguous tweets is stored
pairwiseRankSetAmbiguousTweetsResultsFile = pairwiseDir + "PairwiseRankSetAmbiguousTweets.txt"
# output file for set of ranked ambiguous tweets list
pairwiseRankSetAmbiguousTweetsListFile = pairwiseDir +"PairwiseRankSetAmbiguousTweets.ListObj"
# where text of set of ranked all tweets is stored
pairwiseRankSetAllTweetsResultsFile = pairwiseDir + "PairwiseRankSetAllTweets.txt"
# output file for set of ranked all tweets list
pairwiseRankSetAllTweetsListFile = pairwiseDir + "PairwiseRankSetAllTweets.ListObj"

# where text of labeled set of ambiguous tweets is stored
labeledAmbiguousTweetSetTextResultsFile = labelDir + "LabeledAmbiguousTweetSet.txt"
# output file for labeled set of ambiguous tweets
labeledAmbiguousTweetSetListFile = labelDir + "LabeledAmbiguousTweetSet.ListObj"
# file for int variable tracking number of labels completed
labelCountFile = labelDir + "LabelCount.var"
# file for list tracking skipped indexes in LabelMaker
labelSkippedFile = labelDir + "LabelSkipped.ListObj"
# file for storing sorted bayes predictions text results
sortedBayesPredictionsTextResultsFile = labelDir + "SortedBayesPredictions.txt"
# file for storing sorted bayes predictions list
sortedBayesPredictionsListFile = labelDir + "SortedBayesPredictions.ListObj"
# file for storing list sizes for BayesByWordDictCreator.py as text
trainingDataSizesTextFile = nbTrainingDir + "NbTrainingDataSizes.txt"
# file for storing list sizes for BayesByWordDictCreator.py as list
trainingDataSizesListFile = nbTrainingDir + "NbTrainingDataSizes.ListObj"
# file for storing sorted predictions lists by word as dict object
sortedPredictionsListsByWordFile = nbTrainingDir + "SortedPredictionsListsByWord.DictObj"
# file for storing tweets sorted from NaiveBayes.py results
trainingDataFromBayesToLabelFile = nbTrainingDir + "NbTrainingDataToLabel.ListObj"
# where text of labeled set of bayes tweets is stored
labeledBayesTweetSetTextResultsFile = nbTrainingDir + "LabeledAmbiguousTweetSet.txt"
# output file for labeled set of bayes tweets
labeledBayesTweetSetListFile = nbTrainingDir + "LabeledAmbiguousTweetSet.ListObj"
# file for int variable tracking number of labels completed
labelCountBayesFile = nbTrainingDir + "LabelCount.var"
# file for list tracking skipped indexes in LabelMaker
labelSkippedBayesFile = nbTrainingDir + "LabelSkipped.ListObj"
# file for storing sorted predictions sets by word as dict object
sortedPredictionsSetsByWordFile = nbTrainingDir + "SortedPredictionsSetsByWord.DictObj"
# file for storing set sizes for BayesByWordDictRankSet.py as text
trainingDataSetSizesTextFile = nbTrainingDir + "NbTrainingDataSetSizes.txt"
# file for storing set sizes for BayesByWordDictRankSet.py as list
trainingDataSetSizesListFile = nbTrainingDir + "NbTrainingDataSetSizes.ListObj"
# where text of labeled word dict set is stored
labeledWordDictSetTextResultsFile = nbTrainingDir + "LabeledWordDictSet.txt"
# output file for labeled word dict set as list object
labeledWordDictSetListFile = nbTrainingDir + "LabeledWordDictSet.ListObj"
# output file for labeled word dict set as dict object by word
labeledWordDictSetByWordFile = nbTrainingDir + "LabeledWordDictSetByWord.DictObj"
# file for int variable tracking number of labels completed
labelCountWordDictFile = nbTrainingDir + "LabelCountWordDict.var"
# file for list tracking skipped indexes in LabelMaker
labelSkippedWordDictFile = nbTrainingDir + "LabelSkippedWordDict.ListObj"
# file for storing combined labeled tweets from all files
labeledTweetsFile = labelDir + "LabeledTweets.ListObj"

# file for w2vModel created from AllTokenizedTweets.DictObj
word2VecATTModelFile = w2vModelsDir + "word2VecATT.model"
# file for w2vModel text results created from AllTokenizedTweets.DictObj
word2VecATTResultsFile = w2vModelsDir + "word2VecATTResults.txt"
# file for w2vModel created from PairwiseRankSetAmbiguousTweets.ListObj
word2VecPRSAmbModelFile = w2vModelsDir + "word2VecPRSAmb.model"
# file for w2vModel text results created from PairwiseRankSetAmbiguousTweets.ListObj
word2VecPRSAmbResultsFile = w2vModelsDir + "word2VecPRSAmbResults.txt"
# file for w2vModel created from PairwiseRankSetAllTweets.ListObj
word2VecPRSAllModelFile = w2vModelsDir + "word2VecPRSAll.model"
# file for w2vModel text results created from PairwiseRankSetAmbiguousTweets.ListObj
word2VecPRSAllResultsFile = w2vModelsDir + "word2VecPRSAllResults.txt"
# file for storing w2vSVM positive results by ID
word2VecSVMPosLabelsByIDFile = labelDir + "word2VecSVMPosLabelsByID.ListObj"
# object file for storing dict for location by tweet id
allTweetsLocFile = localDir + "LocByID.DictObj"
# text file for results of TweetLocator.py
identifiedTweetLocResultsFile = localDir + "identifiedTweetLocResults.txt"