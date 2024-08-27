# all us state abbreviations
statesFile = open('stateAbbreviations.txt', 'r')
stateAbb = [w.strip().lower() for w in statesFile.readlines()]

# open english words file 
dict_file = open('words.txt', 'r')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiouy'
words = [w.strip().lower() for w in dict_file.readlines()]

goodWords = []

for word in words:
	if len(word) % 2 == 0:  #only check even words
		thisWordOK = True
		for idx in range(0, len(word), 2):
			theseTwo = word[idx:idx+2]		# get the current two letters

			theseOK = False

			for thisAbbr in stateAbb:
				if theseTwo == thisAbbr:
					theseOK = True

			if not theseOK:
				thisWordOK = False
				break

		# when done iterating
		if thisWordOK:
			goodWords.append(word)


print('all possible words: ')
for goodWord in goodWords:
	print(goodWord)