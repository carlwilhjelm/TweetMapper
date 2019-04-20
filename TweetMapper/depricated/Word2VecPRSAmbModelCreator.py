import gensim
from LocalDir import *
import pickle

with open(pairwiseRankSetAmbiguousTweetsListFile, 'rb') as f:
    pairwiseRankSet = pickle.load(f)
print(len(pairwiseRankSet))

onlyTokens = []
for ID, textScoreTuple in pairwiseRankSet:
    onlyTokens.append(textScoreTuple[0])

model = gensim.models.Word2Vec(onlyTokens, size=150, window=10, min_count=2, workers=10)
model.train(onlyTokens, total_examples=len(onlyTokens), epochs=10)

with open(word2VecPRSAmbModelFile, 'wb') as f:
    model.save(f)

textResult = ""
for word in ["good", "bad", "dope", "crack", "weed", "oxy", "opioid"]:
    try:
        similar = model.wv.most_similar(positive=word)
        textResult += word + "\n " + " ".join([word + ": " + str(score) + '\n' for word, score in similar]) + "\n\n"
    except:
        continue

with open(word2VecPRSAmbResultsFile, 'w') as f:
    f.write(textResult)
