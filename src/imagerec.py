from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
import time
from collections import Counter



def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0, 10)
    versionWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionWeHave:
            #print (str(eachNum)+'.'+str(eachVer))
            imgFilePath = 'EColi/'+ str(eachNum)+'.'+str(eachVer)+'.jfif'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())

            lineToWrite = str(eachNum) + '::'+eiar1 + '\n'
            numberArrayExamples.write(lineToWrite)




def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value



def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x+y, eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)

    balance = reduce(lambda x, y: x+y, balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x+y, eachPix[:3])/len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
             

            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
           
    return newAr   

def whatPicisThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExamples in loadExamps:
        if len(eachExamples) > 3:
            splitEx = eachExamples.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')


            eachPixInQ = inQuestion.split('],')

            x=0

            while x <len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x += 1
    
    print (matchedAr)
    x = Counter(matchedAr)
    print(x)
    

whatPicisThis('EColi/test.jfif')







            
