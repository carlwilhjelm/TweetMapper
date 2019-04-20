import gensim
from sklearn.metrics import accuracy_score
from LocalDir import *
import pickle
import random
import numpy as np
from sklearn.svm import SVC


w2vModel = gensim.models.Word2Vec.load(word2VecPRSAllModelFile)

with open(labeledTweetsFile, 'rb') as f:
    data = pickle.load(f)

def trainTestPartition(listIn):
    n = len(listIn)
    m = 5
    random.shuffle(listIn)
    train = listIn[:-(n//m)]
    test = listIn[-(n//m):]
    return train, test


layerSize = w2vModel.layer1_size
print("Results for w2vPRSAllModel")
print(w2vModel)

vectorizedData = []
for label, tokens, ID in data:
    # array of vectors for each tokenized word
    arr = []
    for t in tokens:
        try:
            arr.append(w2vModel[t])
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
    mean = [label]
    for i in range(len(sum)):
        mean.append(sum[i] / layerSize)

    vectorizedData.append(mean)

# number of cycles
k = 1
# param SVC C
svc_C = 500
# initialize values for calculating accuracy, specificity, and sensitivity
avgAccuracy, lowestAccuracy, highestAccuracy = 0, 1, 0
avgSpecificity, lowestSpecificity, highestSpecificity = 0, 1, 0
avgSensitivity, lowestSensitivity, highestSensitivity = 0, 1, 0

for i in range(k):
    # parse data into separate training and testing sets
    train, test = trainTestPartition(vectorizedData)
    train = np.array(train)
    test = np.array(test)
    trainY = train[:, 0]
    trainX = train[:, 1:]
    testY = test[:, 0]
    testX = test[:, 1:]
    svcModel = SVC(kernel='linear', C=svc_C)
    svcModel.fit(trainX, trainY)
    pred = svcModel.predict(testX)
    # record accuracy results
    accuracy = accuracy_score(testY, pred, normalize=True)
    if accuracy < lowestAccuracy: lowestAccuracy = accuracy
    if accuracy > highestAccuracy: highestAccuracy = accuracy
    avgAccuracy += accuracy

    # record sensitivity TP/P and specificity TN/N
    TP, P, TN, N = 0, 0, 0, 0
    for j in range(len(pred)):
        if pred[j] == "1":
            P += 1
            if testY[j] == "1":
                TP += 1
        else:
            N += 1
            if testY[j] == "0":
                TN += 1
    sensitivity = TP/P
    specificity = TN/N

    # record sensitivity results
    if sensitivity < lowestSensitivity: lowestSensitivity = sensitivity
    if sensitivity > highestSensitivity: highestSensitivity = sensitivity
    avgSensitivity += sensitivity

    # record specificity results
    if specificity < lowestSpecificity: lowestSpecificity = specificity
    if specificity > highestSpecificity: highestSpecificity = specificity
    avgSpecificity += specificity


print("SVC C param = " + str(svc_C))
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



