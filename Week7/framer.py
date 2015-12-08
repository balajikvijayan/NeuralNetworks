__author__ = 'mike.bowles'
import numpy as np
import cPickle as pickle


def formatter(histLength=1, predLag=5, trainFrac=0.80):
    dataList = []
    dataFile = open('table_a.csv')
    for line in dataFile:
        lineList = line.strip().split(',')
        dataList.append([float(x) for x in lineList[2:7]])
    #define pointer that starts at histLength and runs to length - predLag
    attr = []
    y = []
    for iPoint in range(histLength, len(dataList) - predLag):
        #flatten history before iPoint and calculate change in closing price between iPoint and iPoint + predLag
        attrLine = []
        for i in range(iPoint-histLength, iPoint):
            attrLine += dataList[i]
        #attrLine = [temp + dataList[i] for i in range(iPoint-histLength, iPoint)]
        attr.append(attrLine)
        currClse = dataList[iPoint][3]
        futClse = dataList[iPoint + predLag][3]
        yVal = futClse - currClse
        y.append(yVal)  #difference in closing prices
    #calculate index for start of training set
    #trainStart = int(trainFrac * len(attr))
    #xTr = attr[:trainStart]; xTe = attr[trainStart:]; yTr = y[:trainStart]; yTe = y[trainStart:]
    #xTr = np.array(attr)
    #yTr = np.array(y)
    return  attr, y    #take raw pricing data, return numpy array of attributes and labels


x, y = formatter()

print len(x), len(x[0]), len(y), np.std(np.array(y))
pickle.dump((x, y), open('stockTT.bin', 'wb'))