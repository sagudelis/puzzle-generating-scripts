# globals
inputFile = 'knownUniverses.txt'
outputFile = 'allUniverses.txt'
universeNumbersArray = []
universeDataArray = []
writeFile = open(outputFile, 'w')

# get the data about each planet and store keyed
# function to get data from the given file
alldata = open(inputFile, 'r', encoding='utf8')
thisdata = alldata.readlines()
alldata.close()

# store keyed data
for idx in range(len(thisdata)-1):
    if 'Earth' in thisdata[idx]:
        earthNum = int(thisdata[idx].split('-')[1].split(':')[0])

        # print(f'{earthNum}')
        earthData = ''

        j = idx + 1
        while 'Earth' not in thisdata[j]:
            earthData += '\t' + thisdata[j]
            j += 1

            if j >= len(thisdata):
                break

        # print('appending')
        universeNumbersArray.append(earthNum)
        universeDataArray.append(earthData)


# 'Earths {} to {}:'
# '\tEarth {}:'
# '\t\t Info'

# for i in range(1, 999, 1):
#     thisHundredsText = ''
#     hundred = i
#     # nextHundred = (hundred + 99 if hundred < 98 else 99)
#     heading = f'Earth {hundred}:'
#     thisHundredsText += heading
#
#     noData = True
#     # while the first element is in the range of numbers
#     while len(universeNumbersArray) > 0 and universeNumbersArray[0] == hundred: # and universeNumbersArray[0] < nextHundred:
#         noData = False
#         # add the subheading and data
#         # subheading = f'\tEarth {universeNumbersArray[0]}:\n'
#         data = '\n' + universeDataArray[0]
#         # print(data)
#         thisHundredsText += data
#
#         # remove the first element of the array
#         universeNumbersArray.pop(0)
#         universeDataArray.pop(0)
#
#         if len(universeNumbersArray) == 0:
#             break
#
#     if noData:
#         thisHundredsText += ' Uncharted\n'
#
#     thisHundredsText += '\n'
#     writeFile.write(thisHundredsText)
#     # print(thisHundredsText)
#
# for i in range(1000, 9999, 10):
#     thisHundredsText = ''
#     hundred = i
#     nextHundred = (hundred + 9 if hundred < 9989 else 9999)
#     heading = f'Earths {hundred} to {nextHundred}: '
#     thisHundredsText += heading
#
#     noData = True
#     # while the first element is in the range of numbers
#     while len(universeNumbersArray) > 0 and universeNumbersArray[0] >= hundred and universeNumbersArray[0] < nextHundred:
#         noData = False
#         # add the subheading and data
#         subheading = f'\tEarth {universeNumbersArray[0]}:\n'
#         data = '\n' + universeDataArray[0]
#         # print(data)
#         thisHundredsText += subheading + data
#
#         # remove the first element of the array
#         universeNumbersArray.pop(0)
#         universeDataArray.pop(0)
#
#         if len(universeNumbersArray) == 0:
#             break
#
#     if noData:
#         thisHundredsText += 'Uncharted\n'
#
#     thisHundredsText += '\n'
#     writeFile.write(thisHundredsText)
# #     # print(thisHundredsText)
#
# for i in range(10000, 999999, 100):
#     thisHundredsText = ''
#     hundred = i
#     nextHundred = (hundred + 99 if hundred < 999899 else 999999)
#     heading = f'Earths {hundred} to {nextHundred}: '
#     thisHundredsText += heading
#
#     noData = True
#     # while the first element is in the range of numbers
#     while len(universeNumbersArray) > 0 and universeNumbersArray[0] >= hundred and universeNumbersArray[0] < nextHundred:
#         noData = False
#         # add the subheading and data
#         subheading = f'\tEarth {universeNumbersArray[0]}:\n'
#         data = '\n' + universeDataArray[0]
#         # print(data)
#         thisHundredsText += subheading + data
#
#         # remove the first element of the array
#         universeNumbersArray.pop(0)
#         universeDataArray.pop(0)
#
#         if len(universeNumbersArray) == 0:
#             break
#
#     if noData:
#         thisHundredsText += 'Uncharted\n'
#
#     thisHundredsText += '\n'
#     writeFile.write(thisHundredsText)
#
# for i in range(1000000, 9999999, 1000):
#     thisHundredsText = ''
#     hundred = i
#     nextHundred = (hundred + 999 if hundred < 9998999 else 9999999)
#     heading = f'Earths {hundred} to {nextHundred}: '
#     thisHundredsText += heading
#
#     noData = True
#     # while the first element is in the range of numbers
#     while len(universeNumbersArray) > 0 and universeNumbersArray[0] >= hundred and universeNumbersArray[0] < nextHundred:
#         noData = False
#         # add the subheading and data
#         subheading = f'\tEarth {universeNumbersArray[0]}:\n'
#         data = '\n' + universeDataArray[0]
#         # print(data)
#         thisHundredsText += subheading + data
#
#         # remove the first element of the array
#         universeNumbersArray.pop(0)
#         universeDataArray.pop(0)
#
#         if len(universeNumbersArray) == 0:
#             break
#
#     if noData:
#         thisHundredsText += 'Uncharted\n'
#
#     thisHundredsText += '\n'
#     writeFile.write(thisHundredsText)

for i in range(0, 9999999, 100):
    thisHundredsText = ''
    hundred = i
    nextHundred = (hundred + 99 if hundred < 9999899 else 9999999)
    heading = f'Earths {hundred} to {nextHundred}:\n'
    thisHundredsText += heading

    noData = True
    # while the first element is in the range of numbers
    while len(universeNumbersArray) > 0 and universeNumbersArray[0] >= hundred and universeNumbersArray[0] < nextHundred:
        noData = False
        # add the subheading and data
        subheading = f'\tEarth {universeNumbersArray[0]}:\n'
        data = universeDataArray[0]
        # print(data)
        thisHundredsText += subheading + data

        # remove the first element of the array
        universeNumbersArray.pop(0)
        universeDataArray.pop(0)

        if len(universeNumbersArray) == 0:
            break

    if noData:
        thisHundredsText += '\tUncharted\n'

    thisHundredsText += '\n'
    writeFile.write(thisHundredsText)
    # print(thisHundredsText)

writeFile.close()
# save file


