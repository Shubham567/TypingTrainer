import random



def genString(sampleFileName, numWords = 4):
    dictFile = open(sampleFileName,"r")
    dict = list(dictFile)

    dictSize = len(dict)

    testStr = ""
    for i in range(0, numWords):
        rndNum = random.randrange(0, dictSize, 1)
        testStr = testStr + dict[rndNum].rstrip("\n")
        if i != numWords - 1:
            testStr = testStr + " "

    return testStr


def getAccuracy(testStr, typeStr, timeElapsedInMilli):
    typeStrLen = len(typeStr)
    testStrLen = len(testStr)
    correct = 0
    for i in range(0, testStrLen):
        if i < typeStrLen:
            if typeStr[i] == testStr[i]:
                correct = correct + 1

    accuracy = correct / testStrLen * 100

    charPerMin = len(typeStr) / timeElapsedInMilli * 1000 * 60
    return accuracy,charPerMin
