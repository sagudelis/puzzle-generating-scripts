
# open english words file 
dict_file = open('words.txt', 'r')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiouy'
words = [w.strip().lower() for w in dict_file.readlines()]


def get_letter_freqs(word):
	freqs = {}
	for i in word:
		if i in freqs:
			freqs[i] += 1
		else:
			freqs[i] = 1

	return freqs


def remove_letters(word, freqs):
	letters_to_remove = []
	for let in freqs:
		if freqs[let] >= 3:
			letters_to_remove.append(let)

	for let in letters_to_remove:
		word = word.replace(let, '')

	return word, letters_to_remove


# def remove_duplicates(double_triples, double_triples_base, lets_removed):
# 	for w in double_triples_base:
# 		indices = [i for i, x in enumerate(double_triples_base) if x == w]
#
# 		if len(indices) > 1:
# 			num_deleted = 0
# 			for index in indices:
# 				idx = index - num_deleted
# 				del double_triples[idx]
# 				del double_triples_base[idx]
# 				del lets_removed[idx]
# 				num_deleted += 1
#
#
# def first_last_only(double_triples, double_triples_base, lets_removed):
# 	i = 0
# 	while i in range(len(double_triples_base)):
# 		if double_triples[i][0] in lets_removed[i] or double_triples[i][len(double_triples[i])-1] in lets_removed[i]:
# 			# if i >= len(double_triples) - 1:
# 			# 	return
# 			del double_triples[i]
# 			del double_triples_base[i]
# 			del lets_removed[i]
# 			# i -= 1
# 		else:
# 			i += 1
#
#
# def only_vowels(double_triples, double_triples_base, lets_removed):
# 	i = 0
# 	while i in range(len(lets_removed)):
# 		for j in range(len(lets_removed[i]) - 1):
# 		if lets_removed[i][0] not in vowels or lets_removed[i][1] not in vowels:
# 			del double_triples[i]
# 			del double_triples_base[i]
# 			del lets_removed[i]
# 		else:
# 			i += 1


double_triples = []
double_triples_base = []
lets_removed = []
for word in words:
	if word[-6:] == 'nesses':
		continue
	freqs = get_letter_freqs(word)
	# triples = freqs.items([count >= 3 for count in freqs.values()])
	num_triples = sum([count >= 3 for count in freqs.values()])
	if num_triples >= 2:
		double_triples += [word]
		remove_out = remove_letters(word, freqs)
		double_triples_base += [remove_out[0]]
		lets_removed += [remove_out[1]]

print(f'before removing duplicates: {len(double_triples)} words found')

# for w in range(len(double_triples)):
# 	print(f'{double_triples[w]}, {double_triples_base[w]}')
#
# remove_duplicates(double_triples, double_triples_base, lets_removed)
# first_last_only(double_triples, double_triples_base, lets_removed)
# only_vowels(double_triples, double_triples_base, lets_removed)
#
# print(f'after removing duplicates: {len(double_triples)} words found')

for w in range(len(double_triples)):
	print(f'{double_triples[w]}, {double_triples_base[w]}, {lets_removed[w]}')
