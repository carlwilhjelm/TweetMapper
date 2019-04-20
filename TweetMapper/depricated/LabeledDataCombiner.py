# DEPRECATED
import pickle

with open(r"D:\School\GSU\Skums\SacredTrainingData\TM10Labels\LabeledAmbiguousTweetSet.ListObj", 'rb') as f:
    ambigTweetLabels = pickle.load(f)

with open(r"D:\School\GSU\Skums\SacredTrainingData\TM10Labels\LabeledWordDictSet.ListObj", 'rb') as f:
    wordDictLabels = pickle.load(f)

concat = ambigTweetLabels + wordDictLabels

for elem in concat:
    print(elem)

print(len(concat))

with open(r"D:\School\GSU\Skums\SacredTrainingData\TM11Labels\LabeledTweets.ListObj", 'wb') as f:
    pickle.dump(concat, f)

