import random
import string

textList = []
textMap = dict()

with open("source.txt", "r") as file:
    for line in file: 
        #line = line.replace("\n", " ")
        textList.append(line)


fullText = "".join(textList)
strList = list(fullText)
searchLengthIndex = 10
for i in range(len(strList) - 1 - searchLengthIndex):
    subString = ",".join(strList[i:i+searchLengthIndex])
    nextStr = strList[i+searchLengthIndex] + strList[i+1+searchLengthIndex]
    tempDict = textMap.get(subString, dict())
    tempDict.update({nextStr : tempDict.get(nextStr, 0) + 1})
    textMap.update({subString : tempDict})

newText = "What was the president of"
for i in range(1000):
    lastFive = newText[(-1 * searchLengthIndex):]
    newTextList = list(lastFive)
    searchKey = ",".join(newTextList)
    otherDict = textMap.get((searchKey), 0)
    if (otherDict == 0):
        newKey = random.choice(string.ascii_letters)
    elif (otherDict != 0):
        newKey = random.choices(list(otherDict.keys()), weights=otherDict.values(), k=1)[0]
    newText = newText + newKey

print(newText)