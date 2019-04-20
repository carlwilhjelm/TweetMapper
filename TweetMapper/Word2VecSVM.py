import gensim
from LocalDir import *
import pickle
import numpy as np
from sklearn.svm import SVC

def vectorizeData(dataIn, modelIn):
    # create vectorized data from training set, IDs can be ignored
    layerSize = modelIn.layer1_size
    vectorizedData = []
    for labelOrRankScore, tokens, ID in dataIn:
        # array of vectors for each tokenized word
        arr = []
        for t in tokens:
            try:
                arr.append(modelIn[t])
            # if a vector for this word does not exist in the model ignore it
            except KeyError:
                continue
        # if no word in this list has a vector ignore the entire line
        if len(arr) == 0:
            continue
        # otherwise calculate the mean vector
        sum = [0 for i in range(layerSize)]
        for i in range(len(arr)):
            for j in range(layerSize):
                sum[j] += arr[i][j]

        # format = [label, x, y, ..., z]
        mean = [labelOrRankScore]
        for i in range(len(sum)):
            mean.append(sum[i] / layerSize)

        vectorizedData.append(mean)
    return vectorizedData

def word2VecSVM(w2vModelIn, trainingDataIn, testingDataIn):
    # param SVC C usually set to 5000
    svc_C = 5000
    # vectorize training and testing data and convert to numpy arrays
    train = np.array(vectorizeData(trainingDataIn, w2vModelIn))
    test = np.array(vectorizeData(testingDataIn, w2vModelIn))
    trainY = train[:, 0]
    trainX = train[:, 1:]
    testX = test[:, 1:]
    svcModel = SVC(kernel='linear', C=svc_C)
    svcModel.fit(trainX, trainY)
    pred = svcModel.predict(testX)
    posPred = []
    for i in range(len(pred)):
        if pred[i] == '1':
            # append only the ID for each tweet
            posPred.append(testingDataIn[i][2])
    return posPred

# load model
w2vModel = gensim.models.Word2Vec.load(word2VecPRSAllModelFile)
# load training data format [label, tokens, ID]
with open(labeledTweetsFile, 'rb') as f:
    trainingData = pickle.load(f)

# load testing data format dict[ID] = tokens
with open(pairwiseRankAllTweetsListFile, 'rb') as f:
    testingData = pickle.load(f)

posResultsById = word2VecSVM(w2vModel, trainingData, testingData)

with open(word2VecSVMPosLabelsByIDFile, 'wb') as f:
    pickle.dump(posResultsById, f)

