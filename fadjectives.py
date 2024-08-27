import nltk
from collections import defaultdict
from better_profanity import profanity

nltk.download('brown')
nltk.download('universal_tagset')
nltk.download('wordnet')

from nltk.corpus import wordnet as wn

# for synset in list(wn.all_synsets('a')):
#     print(synset.lemma_names())

# print(profanity._default_wordlist_filename)

all_adjectives = [word for synset in wn.all_synsets(wn.ADJ) for word in synset.lemma_names()]
for adjective in all_adjectives:
    if adjective.lower()[0] == 'm':
        if profanity.contains_profanity(adjective.lower()):
            print(adjective)

# wordtags = nltk.ConditionalFreqDist((w.lower(), t) for w, t in nltk.corpus.brown.tagged_words(tagset="universal"))
#
# word_pos = defaultdict(list)
# for word in open("words.txt"):
#     for pos in wordtags["report"]:
#         word_pos[pos.lower()].append(word)
#
#
# for pos in word_pos:
#     with open(f"{pos}.txt", "w") as f:
#         f.write("".join(word_pos[pos]))


# dictfile = open('wordDictionary.txt', 'r')
# allwords = []
# for eachLine in dictfile.readlines():
#     split = eachLine.split('|')
#     # print(split[0])
#     # print(split[1])
#     if split[0][0].lower() == 'f' and split[1].lower() == 'adjective':
#     #     print(split[0].lower())
#     #     print(split[1])
#     # if split[1].lower() == 'adjective':
#         print(split[0].lower())

