# from tqdm import tqdm
# import timeout
import time
file1 = open('words.txt', 'r')
lines = file1.readlines()

possibleWords = []
outlines = []

for line in lines:
# for line in ['abdominoanterior']:
    word = line.strip()
    if len(word) > 8:
# word = 'electron'

        desiredOuts = [ord(char) - 96 for char in word.lower()]
        # print(desiredOuts)
        # desiredOuts = [3, 15, 21, 16, 12, 1, 14, 7]
        possibleIns = list(range(1, len(desiredOuts) + 1))
        # print(possibleIns)

        allPossible = []
        for res in desiredOuts:
            thesePossible = []

            for in1 in possibleIns:
                for in2 in possibleIns:
                    if in1 + in2 == res:
                        thesePossible.append([in1, '+', in2])
                    if in1 - in2 == res:
                        thesePossible.append([in1, '-', in2])
                    if in1 * in2 == res:
                        thesePossible.append([in1, '*', in2])
                    if in1 / in2 == res:
                        thesePossible.append([in1, '/', in2])
                    # if in1 ** in2 == res:
                    #     thesePossible.append([in1, '^', in2])

            allPossible.append(thesePossible)

            # print(f'For {res}:')
            # for each in thesePossible:
            #     print(each)

        # sort possible by list size
        lens = [len(x) for x in allPossible]
        # print(lens)
        # allPossible.sort(key=len)

        sortedNums = desiredOuts
        sortedNums = [x for _, x in sorted(zip(lens, sortedNums))]
        # print(sortedNums)

        # recursion baby
        # @timeout(10)
        def findNextOutfit(usedShirts, usedPants, symbs, allPossible):
            global word
            if time.time() > start + timeout_limit:
                return 0

            if len(usedShirts) == len(word) or len(allPossible) == 0:   # end of recursive call
                outlines.extend([f'Solution for {word}\n'
                                 f'Used Shirts: {usedShirts}\n'
                                 f'Used Pants: {usedPants}\n'
                                 f'symbs: {symbs}\n\n'])
                # print(f'Solution for {word}')
                # print(f'Used Shirts: {usedShirts}')
                # print(f'Used Pants: {usedPants}')
                # print(f'symbs: {symbs}\n')
                print(word)
                possibleWords.append(word)
                # for each in usedShirts:
                return True
            else:
                # newS = usedShirts.copy()
                # newP = usedPants.copy()
                noOutfits = True
                for eachOutfit in allPossible[0]:       # look at the next set of outfit options
                    if eachOutfit[0] not in usedShirts and eachOutfit[2] not in usedPants:
                        noOutfits = False
                        usedShirts.append(eachOutfit[0])
                        usedPants.append(eachOutfit[2])
                        symbs.append(eachOutfit[1])
                        # if len(allPossible) > 1:
                        if not findNextOutfit(usedShirts, usedPants, symbs, allPossible[1:]):
                            usedShirts.pop()
                            usedPants.pop()
                            symbs.pop()
                        else:
                            return True

                        # else:
                        #     findNextOutfit(usedShirts, usedPants, [])
                if noOutfits:
                    # print('no possible outfits - s')
                    # print(f'Used Shirts: {usedShirts}')
                    # print(f'Used Pants: {usedPants}')
                    # print('no possible outfits - e')
                    return False

        start = time.time()
        timeout_limit = 0.5

        findNextOutfit([], [], [], allPossible)

    # # narrowing it down
    # for outfits in allPossible:
    #     for possibleOutfits in outfits:


outfile = open('barbieWord.txt', 'w')
outfile.writelines(outlines)
outfile.close()