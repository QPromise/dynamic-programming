import os
import random

def genNFile(fileNum):
    numCount=fileNum
    numRange=3*numCount

    tmpList=random.sample(range(numRange), numCount)

    i=0
    filePath=""+str(numCount)+".txt"
    with open(filePath, "w", encoding="utf8") as f:
       while i<numCount:
        f.write(str(tmpList[i]))
        f.write("\n")
        i=i+1

genNFile(11000)