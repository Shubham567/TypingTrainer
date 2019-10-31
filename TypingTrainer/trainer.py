import generator
import common
import time
import os

attempts = 0
accuracySum = 0
cpmSum = 0
print("\nTyping Trainer by SS7 v 0.1 \n")
while True:
    attempts = attempts + 1

    testStr = generator.genString(common.dictionaryFile, common.wordCount)
    print(testStr)
    bfrTime = time.time() * 1000
    testStrLen = len(testStr)
    typeStr = ""
    try:
        typeStr = input()
    except (KeyboardInterrupt, SystemExit):
        if attempts < 2:
            print("  Interrupted. Not enough data to show average.")
        else:
            print("  Average-Accuracy: " + str(accuracySum / (attempts - 1)) + " Average-CPM:" + str(int(cpmSum / (attempts - 1))))
        exit(0)

    afterTime = time.time() * 1000

    timeElapsed = afterTime - bfrTime

    accuracy, charPerMin = generator.getAccuracy(testStr, typeStr, timeElapsed)
    accuracySum = accuracySum + accuracy
    cpmSum = cpmSum + charPerMin

    if attempts % common.clearScreen == 0:
        os.system("clear")

    print("\nAccuracy: " + str(accuracy) + "% Speed: " + str(int(charPerMin)) + "cpm\n")
