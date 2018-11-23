#coding=utf-8
import operator
from math import log
import time
import os, sys
import string

def createDataSet(trainDataFile):
    print (trainDataFile)
    dataSet = []
    try:
        fin = open(trainDataFile)
        for line in fin:
            line = line.strip()
            cols = line.split('\t')
            row = [cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7], cols[8], cols[9], cols[10], cols[0]]
            dataSet.append(row)
            #print row
    except:
        print ('Usage xxx.py trainDataFilePath')
        sys.exit()
        labels = ['cip1', 'cip2', 'cip3', 'cip4', 'sip1', 'sip2', 'sip3', 'sip4', 'sport', 'domain']
    print ('dataSetlen', len(dataSet))
        return dataSet, labels

#calc shannon entropy of label or feature
def calcShannonEntOfFeature(dataSet, feat):
    numEntries = len(dataSet)
    labelCounts = {}
    for feaVec in dataSet:
        currentLabel = feaVec[feat]
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1    #last col is label
    baseEntropy = calcShannonEntOfFeature(dataSet, -1)
    bestInfoGainRate = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob *calcShannonEntOfFeature(subDataSet, -1)    #calc conditional entropy
        infoGain = baseEntropy - newEntropy
    　　 iv = calcShannonEntOfFeature(dataSet, i)
        if(iv == 0):    #value of the feature is all same,infoGain and iv all equal 0, skip the feature
        continue
    　　 infoGainRate = infoGain / iv
        if infoGainRate > bestInfoGainRate:
            bestInfoGainRate = infoGainRate
            bestFeature = i
    return bestFeature

            

#feature is exhaustive, reture what you want label

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    return max(classCount)         

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) ==len(classList):    #all data is the same label
        return classList[0]
    if len(dataSet[0]) == 1:    #all feature is exhaustive
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    if(bestFeat == -1):        #特征一样，但类别不一样，即类别与特征不相关，随机选第一个类别做分类结果
    return classList[0] 
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree

    

def main():
    if(len(sys.argv) < 3):
    print ('Usage xxx.py trainSet outputTreeFile')
    sys.exit()
    data,label = createDataSet(sys.argv[1])
    t1 = time.clock()
    myTree = createTree(data,label)
    t2 = time.clock()
    fout = open(sys.argv[2], 'w')
    fout.write(str(myTree))
    fout.close()
    print('execute for ',t2-t1) 

if __name__=='__main__':
    main()

