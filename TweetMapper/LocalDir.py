# maintains directory structure of files

# source file for tweets
sourceDir = "D:\School\GSU\Skums\\tweets\APIStream.2018.09.17\\"
# destination file for results
localDir = sourceDir + "results\\"
# file path for unambiguous dictionary
unambiguousWordsListFile = "D:\School\GSU\Skums\dictionary\metaDictUnambiguous.ListObj"
# path for pairwise results
pairwiseDir = localDir + "\pairwiseResults\\"
# where dict of full tweets by id is stored
rawTweetByIdDictFile = localDir + "RawTweetByID.DictObj"
# where text of lang filter results are stored
langFilterTextResultsFile = localDir + "LangFilterResults.txt"
# where full tweets filtered by language dictionary obj is stored
tweetByIdDictFile = localDir + "LangFilteredTweetByID.DictObj"
# where text of mapper results is stored
mapperTextResultsFile = localDir + "Mapping.txt"
# where unambiguous tweets results obj is stored
unambiguousTokenizedTweetsDictFile = localDir + "UnambiguousTokenizedTweets.DictObj"
# where ambiguous tweets results obj is stored
ambiguousTokenizedTweetsDictFile = localDir + "AmbiguousTokenizedTweets.DictObj"
# where tokenized tweets dict obj is stored
allTokenizedTweetsDictFile = localDir + "AllTokenizedTweets.DictObj"
# where text by ID dict obj is stored
textByIdDictFile = localDir + "TextByID.DictObj"
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
