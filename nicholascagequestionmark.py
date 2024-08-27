file1 = open('commonwords.txt', 'r')
lines = file1.readlines()

phrase1 = 'STEALTHEDECLARATIONFROMSOUTHPAWCAFESHED'.lower()
phrase2 = 'VERBPREFIXSECEDESUNION'.lower()

# make an empty dictionary to hold possible words
pWordsDict = {}
pPreDict = {}
for uniqLetter in set(phrase2):     # each unique letter in phrase 2
    pWordsDict[uniqLetter] = []
    pPreDict[uniqLetter] = []

# lines.reverse()
for line in lines:
    word = line.strip().lower()
    if len(word) > 0 and sum([*map(word.lower().count, "aeiou")]) > 0:
        for letter in phrase2:
            if letter in word:
                preceeding = word.split(letter)[0]
                if preceeding in phrase1:   #len(preceeding) > 0 and
                    if preceeding not in pPreDict[letter]:
                        # preceedList.append(preceeding)
                        # print(f'word = {word}: {preceeding}{letter.upper()}')
                        pWordsDict[letter].append(word)
                        pPreDict[letter].append(preceeding)
                    # else:
                    #     breakpoint()

# sort dict by length of preceeding characters
for letter in pPreDict:
    letList = pPreDict[letter]
    sortedList = sorted(letList, key=lambda x: len(x))
    sortedList.reverse()
    pPreDict[letter] = sortedList


def findLetters(curPhrase1, curPhrase2, wordList, singleCount):
    global pPreDict
    global allCombos
    global comboSLs

    # based on phrase length, end recursion
    if len(curPhrase1) == 0 and len(curPhrase2) == 0:
        thisCombo = ' '.join(wordList)
        if singleCount < 10:
            if thisCombo not in allCombos:
                print(thisCombo)
                allCombos.append(thisCombo)
                comboSLs.append(singleCount)
        return  # found good pair
    elif len(curPhrase1) == 0:  # if phrase 1 is complete, just need a word that starts with the last letter
        thisCombo = ' '.join(wordList) + ' ' + curPhrase2.upper()
        if len(curPhrase2) + singleCount < 10:
            if thisCombo not in allCombos:
                print(thisCombo)
                allCombos.append(thisCombo)
                comboSLs.append(len(curPhrase2) + singleCount)
        else:
            print(curPhrase2)
        return
    elif len(curPhrase2) == 0:  # if phrase 2 is complete and 1 is not, not gonna work
        # print(f"curPhrase1 = {curPhrase1}, {wordList[:4]}")
        return
    elif singleCount > 5:
        return

    # get the corresponding words for the first word of the remaining string
    someWords = pPreDict[curPhrase2[0]]
    for eachPair in someWords:
        # if curPhrase2.startswith('union'):
        #     print(wordList)
        if curPhrase1.startswith(eachPair):
            # if it works, keep recursing
            # print(curPhrase1)
            # print(f'{curPhrase2[0]}: {eachPair}')
            if len(eachPair) > 0:
                # nextP1 = curPhrase1.split(eachPair)[1]
                nextP1 = curPhrase1[len(eachPair):]
                formattedWord = eachPair + curPhrase2[0].upper()  # + eachPair[1].split(eachPair[0])[1][1:]
                nextSCount = singleCount
            else:
                nextP1 = curPhrase1
                nextSCount = singleCount + 1
                # formattedWord = eachPair[0] + curPhrase2[0].upper() + eachPair[1][1:]
                formattedWord = curPhrase2[0].upper()
            nextP2 = curPhrase2[1:]
            # print(f"{eachPair[0]} + {curPhrase2[0].upper()} + {eachPair[1].split(eachPair[0])[1][1:]}")
            # formattedWord = eachPair[0] + curPhrase2[0].upper() + eachPair[1].split(eachPair[0])[1][1:]
            nextWordList = wordList.copy()
            nextWordList.append(formattedWord)
            findLetters(nextP1, nextP2, nextWordList, nextSCount)


# then go through and find combos that work
allCombos = []
comboSLs = []
findLetters(phrase1, phrase2, [], 0)

list1, list2 = zip(*sorted(zip(comboSLs, allCombos)))
print('BEST LISTS:')
for idx in range(len(list1)):
    if list1[idx] < 3:
        if 'rN' not in list2[idx]:
            print(f'{list1[idx]}: {list2[idx]}')

# breakpoint()

