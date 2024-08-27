import pandas as pd
import re
import numpy as np
from collections import defaultdict
import copy
from tqdm import tqdm

# find duplicate boards
boardfile = open('moreboggleboards.txt', 'r')
fullstring = "".join(str(element) for element in boardfile)
boardArray = fullstring.split('\n\n')
myset = list(set(boardArray))
outputboardfile = open('finalboggleboards.txt', 'w')
arr = np.array(myset)
for eachboard in arr:
    outputboardfile.write('\n')
    outputboardfile.write(eachboard)
outputboardfile.close()

# np.savetxt('finalboggleboards.txt', arr)

# read in grids
df = pd.read_excel("Boggle Letter Shapes.xlsx", sheet_name=None, header=None)
letLens = {}

for key in df.keys():  # for each length, find all possible letters
    df[key] = df[key].applymap(lambda x: x.lower() if isinstance(x, str) else x)
    if not df[key].empty:
        letLens[int(key.split(" ")[0])] = [x for x in df[key][0].unique() if str(x) != 'nan']

# make COFFEE shapes
# c3s = [['!c', 'c!', '!c']]
# o4s = [['oo', 'oo'],
#        ['!o!', 'o!o', '!o!']]
# f5s = [['!f', 'f!', 'ff', 'f!']]
# f6s = [['ff', 'f!', 'ff', 'f!'],
#        ['!f', 'f!', 'ff', 'f!', 'f!']]
# e7s = [['ee', 'e!', '!e', 'e!', 'ee'],
#        ['ee', 'e!', 'ee', 'e!', '!e'],
#        ['!e', 'e!', 'e!', 'ee', 'e!', '!e'],
#        ['!ee', 'e!', '!e!', 'e!', '!ee'],
#        ['!e', 'e!', 'ee', 'e!', 'e!', '!e'],
#        ['!e', 'e!', 'ee', 'e!', 'ee']]
# e8s = [['ee', 'e!', 'ee', 'e!', 'ee'],
#        ['!ee', 'e!', 'ee!', 'e!', '!ee']]
c3s = [['!c', 'c!', '!c']]
o4s = [['oo', 'oo'],
       ['!o!', 'o!o', '!o!']]
f5s = [['!f', 'f!', 'ff', 'f!']]
f6s = [['ff', 'f!', 'ff', 'f!']]
e7s = [['ee', 'e!', '!e', 'e!', 'ee'],
       ['!ee', 'e!', '!e!', 'e!', '!ee']]
e8s = [['ee', 'e!', 'ee', 'e!', 'ee'],
       ['!ee', 'e!', 'ee!', 'e!', '!ee']]


# function to make shape from ordered list of indexes
def makeShape(orderedIdx, versSize):
    shape = []
    for i in range(versSize[1]):
        thisList = []
        for j in range(versSize[0]):
            thisList.append('!')
        shape.append(thisList)

    for num, eachIdx in enumerate(orderedIdx):
        shape[eachIdx[0]][eachIdx[1]] = num

    # print(shape)
    return shape


# recursive function to find possible orders for each shape
def findAdjacent(curIdx, unused, ordered, size, versSize):
    if ordered is None:
        pass
    elif unused is None:
        shape = makeShape(ordered, versSize)
        if shape not in theseOrders:
            theseOrders.append(shape)
            # print(shape)
        return
    elif len(unused) == 0 or len(ordered) == size:    # finished iteration
        shape = makeShape(ordered, versSize)
        if shape not in theseOrders:
            theseOrders.append(shape)
            # print(shape)
        return

    for pII, possibleI in enumerate(unused):
        if abs(possibleI[0]-curIdx[0]) <= 1 and abs(possibleI[1]-curIdx[1]) <= 1:
            tempUnused = unused.copy()
            tempUnused.pop(pII)
            tempOrdered = ordered.copy()
            tempOrdered.append(possibleI)
            findAdjacent(possibleI, tempUnused, tempOrdered, size, versSize)


# find all ways to order words in letters
# start at each letter, find adjacent letters,
letters = ['c', 'o', 'f', 'f', 'e', 'e']
allOrders = []
for idx, each in enumerate([c3s, o4s, f5s, f6s, e7s, e8s]):
    theseOrders = []
    for thisVers in each:
        ltf = letters[idx]
        # print(ltf)
        indexes = []
        for row in range(len(thisVers)):
            for let in range(len(thisVers[row])):
                if thisVers[row][let] == ltf:
                    indexes.append([row, let])
        for index in indexes:   # try to start at each letter
            versSize = [len(thisVers[0]), len(thisVers)]
            findAdjacent(index, indexes, [], idx+3, versSize)

    allOrders.append(theseOrders)

# get all words and filter by length
minL = 3 #list(letLens.keys())[0]
maxL = 8 #list(letLens.keys())[-1]
ansLen = 6
wordf = open('feederwords.txt', 'r')
allwords = [re.sub("[^a-zA-Z]+", "", wrd.lower()) for wrd in wordf.readlines()]
# answers = [wrd.strip().lower() for wrd in allwords if len(wrd.strip()) == ansLen]    # filter by length
# answers = list(pd.Series(answers).unique())
# # see if the word can be spelled with letters from letLens
# goodAnswers = []
# for answerWord in answers:
#     goodWord = True
#     for idx, eachLet in enumerate(answerWord):
#         mnLen = idx + 3                # adjust the min length for the next word
#         mxLen = mnLen + 2 if mnLen + 2 <= maxL else maxL    # adjust the max length for the next word
#         letterChoices = []
#         for each in range(mnLen, mxLen+1):
#             letterChoices.extend(letLens[each])
#         if eachLet not in letterChoices:
#             goodWord = False
#     if goodWord:
#         goodAnswers.append(answerWord)
# answers = goodAnswers

# get all possible feeders
letterCombos = ["bb", "oo", "gl", "gl", "lo", "es"]
revLetterCombos = ["bb", "oo", "lg", "lg", "ol", "se"]
letterCombos = ["bb", "oo", "lg", "lg", "ol", "se"]
allFeeders = [wrd.strip() for wrd in allwords if minL <= len(wrd.strip()) <= maxL]
allFeeders = list(pd.Series(allFeeders).unique())
feeders = []
bwFeeders = []
for li in range(len(letters)):
    ll = li+3
    for possible in allFeeders:
        if len(possible) == ll:
            if f'{possible[0]}{possible[-1]}' == letterCombos[li]:
                feeders.append(possible)
            if f'{possible[-1]}{possible[0]}' == revLetterCombos[li]:
                bwFeeders.append(possible)

# feeders = ['scrabble', 'oatmeal', 'lapdog', 'lying', 'oreo', 'bib']
feeders = ['scrounge', 'oatmeal', 'luring', 'lying', 'oreo', 'bib']

# print(feeders)
# fout = open('fwFeeders.txt', 'w')
# fout.writelines([f"{line}\n" for line in feeders])
# quit()
# for possible in allFeeders:
#     if f'{possible[0]}{possible[-1]}' in letterCombos:
#         feeders.append(possible)
#     if f'{possible[-1]}{possible[0]}' in letterCombos:
#         bwFeeders.append(possible)
# feeders = []
d = defaultdict(list)
for w in feeders:
    d[len(w)].append(w)

feedersD = d
# feeders = sorted(feeders, key=len)
# bwFeeders = sorted(bwFeeders, key=len)

# fill feeders into shapes
shapedFeeders = {}    # dictionary, key = feeder, value = list of shaped feeders
# possibleShapes = copy.deepcopy(allOrders)
# if possibleShapes is allOrders: print('uh oh!')
for feeder in feeders:
    # get relevant shape options based on length
    possibleShapes = copy.deepcopy(allOrders)
    possibleShapes = possibleShapes[len(feeder) - 3]
    for eachShape in possibleShapes:
        filledShape = copy.copy(eachShape)
        # print(eachShape)
        for i, row in enumerate(filledShape):
            for j, column in enumerate(row):
                # print(f"{eachShape}\n{i},{j}")
                if type(filledShape[i][j]) == int:
                    filledShape[i][j] = feeder[filledShape[i][j]]
        if feeder not in shapedFeeders.keys():
            shapedFeeders[feeder] = [filledShape]
        else:
            shapedFeeders[feeder].append(filledShape)

# x fill the feeders to the right size, with varied position
# make the base shape
baseshape = []
for i in range(6):
    thisList = []
    for j in range(6):
        thisList.append('!')
    baseshape.append(thisList)
baseshape = np.array(baseshape)

# get filled shapes
filledDict = {}
for thisFeeder in shapedFeeders:
    for eachShape in shapedFeeders[thisFeeder]:
        shapeNP = np.array(eachShape)
        # get x and y size of shape
        xLen = len(eachShape[0])
        yLen = len(eachShape)
        maxX = 7 - xLen
        maxY = 7 - yLen
        # iterate through each possible start point
        for x in range(0, maxX):
            for y in range(0, maxY):
                baseCopy = baseshape.copy()
                baseCopy[y:y+yLen, x:x+xLen] = shapeNP
                if thisFeeder not in filledDict.keys():
                    filledDict[thisFeeder] = [baseCopy]
                else:
                    filledDict[thisFeeder].append(baseCopy)


def anyNeighbors(currentPos, nextLetter, board):
    neighbors = []
    for xns in range(currentPos[0]-1, currentPos[0]+2):
        for yns in range(currentPos[1]-1, currentPos[1]+2):
            if 0 <= xns < len(board) and 0 <= yns < len(board[0]):
                if currentPos != [xns, yns]:
                    neighbors.append([xns, yns])

    # print(neighbors)
    goodNeighbors = []
    for neighbor in neighbors:
        if board[neighbor[0]][neighbor[1]] == nextLetter:
            goodNeighbors.append(neighbor)

    if len(goodNeighbors) == 0:
        return False
    else:
        # print(f"neighbors: {goodNeighbors}")
        return goodNeighbors


def lookForRest(fullFeeder, restOfFeeder, currentPosition, usedPos, board):
    global timesFound
    global allOrdersList

    if len(restOfFeeder) == 0:  # if the whole word has been found
        temppos = usedPos.copy()
        # temppos.append(currentPosition)
        sortedpos = sorted(temppos)
        if sortedpos not in allOrdersList:
            allOrdersList.append(sortedpos)
            # print(sorted)
            # print(temppos)
            timesFound = timesFound+1
        return
    else:
        # print(currentPosition)
        neighborsFound = anyNeighbors(currentPosition, restOfFeeder[0], board)
        if neighborsFound:
            unusedNeighbors = False
            for neighbor in neighborsFound:
                if neighbor not in usedPos:
                    unusedNeighbors = True
                    tempUsedPos = usedPos.copy()
                    tempUsedPos.append(neighbor)
                    # print(restOfFeeder[1:])
                    # print(neighbor)
                    # print(f"used pos = {tempUsedPos}")
                    # if len(restOfFeeder) == 1:
                    #     # return
                    #     lookForRest(fullFeeder, '', neighbor, tempUsedPos, board)
                    # else:
                    lookForRest(fullFeeder, restOfFeeder[1:], neighbor, tempUsedPos, board)
            # if not unusedNeighbors:
            #     return
        else:
            return


# function to find extra occurances of the feeders
def findExtraOccurances(feederList, board):
    global timesFound
    global allOrdersList

    timesFound = 0
    allOrdersList = []
    wordFoundTimes = 0

    # print(feederList)
    # print(board)
    for eachfeeder in feederList:
        # look for the first letter
        allOrdersList = []
        wordFoundTimes = 0
        boardArr = np.array(board)
        flIdx = np.where(boardArr == eachfeeder[0])
        for iii in range(len(flIdx[0])):  # look at neighbors of each occurance of the first letter
            timesFound = 0
            lookForRest(eachfeeder, eachfeeder[1:], [flIdx[0][iii], flIdx[1][iii]], [[flIdx[0][iii], flIdx[1][iii]]], board)
            wordFoundTimes = wordFoundTimes + timesFound

        # print(f"{eachfeeder} found {wordFoundTimes} times")
        if wordFoundTimes > 1:
            # print(f"{eachfeeder} found {wordFoundTimes} times")
            return True
            # pass

    return False


allOrdersList = []
timesFound = 0
testfeederlist = ['sabotage', 'oatmeal', 'lacing', 'lying', 'ohio', 'bob']
testBoard = [['s', 'a', 'b', 'l', 'a', 'l'],
             ['b', 'o', 'a', 'c', 'y', '!'],
             ['o', 't', 'b', 'i', 'n', 'i'],
             ['a', '!', 'm', 'g', 'g', '!'],
             ['g', 'e', '!', '!', 'o', 'i'],
             ['!', 'a', 'l', '!', 'h', 'o']]
# findExtraOccurances(testfeederlist, testBoard)
# quit()


# for each letter:
def getFeeders(currentShape, myFeeder, curList):
    global filledDict
    global usedFeederLists

    # feederListCPY = curList.copy()
    # feederListCPY.append(myFeeder)
    # if feederListCPY in usedFeederLists:
    #     return

    # tempfeederList = curList.copy()
    # tempfeederList.append(myFeeder)
    if findExtraOccurances(curList, currentShape):
        # print(f'failed list: {curList}') #\n{currentShape}')
        return

    allConflict = False
    for thisShape in filledDict[myFeeder]:
        newShape = currentShape.copy()
        # print(thisShape)
        # compare to currentShape and find any conflicting alphabetical indices
        conflicting = False
        for x1 in range(6):
            for y1 in range(6):
                # if they don't conflict
                if thisShape[y1][x1] == currentShape[y1][x1] or thisShape[y1][x1] == '!' or currentShape[y1][x1] == '!':
                    # add to shape
                    # print(f"y = {y1}, x = {x1}")
                    # print(newShape[y1][x1])
                    # print('thisShape')
                    # print(thisShape)
                    # print('thisShape end')
                    newShape[y1][x1] = thisShape[y1][x1] if thisShape[y1][x1] != '!' else newShape[y1][x1]
                else:
                    conflicting = True
        if not conflicting:
            # continue recursion if there are more feeders
            if len(myFeeder) > 3:
                # for feederLen in reversed(feedersD):  # start with biggest values
                # for it in tqdm(range(len(myFeeder)-1)):
                #     newFeeder = feedersD[it]
                for newFeeder in feedersD[len(myFeeder)-1]:
                    feederList = curList.copy()
                    feederList.append(myFeeder)
                    getFeeders(newShape, newFeeder, feederList)
                    # print(newFeeder)
                    # elif len(myFeeder) < 8:
                    #     feederList = curList.copy()
                    #     feederList.append(myFeeder)
                    #     getFeeders(newShape, newFeeder, feederList)
            else:
                feederList = curList.copy()
                feederList.append(myFeeder)
                if not findExtraOccurances(feederList, newShape):
                    # check if any of the feeders can be found multiple times
                    # print('FOUND')
                    usedFeederLists.append(feederList)
                    outputfile = open('allboggleboards.txt', 'a')
                    outputfile.write(f"{feederList}\n")
                    outputfile.write(f"{newShape}\n\n")
                    outputfile.close()
                    print('\n')
                    # print(f"{feederList}")
                    for shapeRow in newShape:
                        print(f"{''.join(shapeRow).upper()}")
                return
        else:
            allConflict = True
            # print('CONFLICT')
    if allConflict:
        # if len(myFeeder) == 3:
        #     print('fails at 3')
            # print(currentShape)
            # print(thisShape)
        return
            # print(myFeeder)
            # if len(myFeeder) > 3:
                # print('fail')
            # return


# outputfile = open('allboggleboards.txt', 'w')
usedFeederLists = []
# for feederLen in reversed(feedersD):     # start with biggest values
for iW, feederWord in enumerate(feedersD[8]):
    # for each feeder in the list
    shapeShape = baseshape.copy()
    print(f"{iW}/{len(feedersD[8])}: {feederWord}")
    getFeeders(shapeShape, feederWord, [])

# shapeShape = baseshape.copy()
# print(filledDict['oenomel'])
# getFeeders(shapeShape, 'scrounge', [])
# print(filledDict['scrounge'])
        # for thisFeeder in filledDict[feederWord]:
#             print(thisFeeder)
            # for each possible filled shape
            # for thisShape in
            # pass
            # fit it into the shape



# # recursive function to get word combos
# def getFeeders(curList, feederList, dLen, letterCmbs):
#     global maxL
#     global ansLen
#     global feederCombos
#
#     # once the list is full
#     if len(curList) >= ansLen:
#         feederCombos.append(curList)    # add list to list of feeder combos
#         # print(curList)  # print the list
#         return
#
#     for idx, feeder in enumerate(feederList[dLen]):
#         # check first and last letter
#         if feeder[0] == letterCmbs[0][0] and feeder[-1] == letterCmbs[0][1]:     # first and last letter work
#             if len(feeder) < 6: print(f"{idx}/{len(feederList[dLen])}: {feeder}")
#             # curList.append(feeder)                  # add the feeder to the list
#             # minLenT = len(feeder) + 1                # adjust the min length for the next word
#             # maxLenT = maxLen + 1 if maxLen < maxL else maxL    # adjust the max length for the next word
#             letterCmbsCpy = letterCmbs.copy()
#             letterCmbsCpy.pop(0)                       # update the list of letter combos for the next word
#
#             # print(f'old: {curList + [feeder]}, feederlist, {minLenT}, {maxLenT}, {letterCmbsCpy}')
#             # print(f'new: {curList}, feederlist, {minLen}, {maxLen}, {letterCmbs}')
#             getFeeders(curList + [feeder], feederList, dLen+1, letterCmbsCpy)     # continue the recursion
#
#     return
#
#
# # get feeder combos
# feederCombos = []
# getFeeders([], feedersD, 3, letterCombos)
# # getFeeders([], bwFeeders, 3, revLetterCombos)
#
# # for each feeder set
# for eachSet in feederCombos:
#     # get the possible shapes from the dict for each feeder
#     for eachFeeder in eachSet:
#         theShapes = shapedFeeders[eachFeeder]
#         print(theShapes[0])









