# Puzzle Generating Scripts
Various scripts to generate answer options/check constraints for puzzles used in the [VT Hunt](https://www.vthunt.com/).

# Scripts currently included:
## barb2.py
Used to generate possible combinations for [Another Fashion Emergency at Los Alamos!](https://www.vthunt.com/past-hunts/march-2024/another-fashion-emergency) with the following constriants:
 - Each article of clothing is associated with an integer 1-n, where n is the number letters in the answer word
 - No two tops use the same integer; no two bottoms use the same integer
 - Belts are associated the four basic mathematical operators: add, subtract, multiply, divide
 - Taking the number of the top outfit (e.g. 8) and using the operator (e.g. minus sign) with the bottom outfit (e.g. 5) will give a final integer (e.g. 3), which gives a letter 

Generates orientations of top/belt/bottom combinations that result in the given answer word.

## chemicalwords.py
Checks a list of words to see which words can be created using only the abbreviations for chemical elements. Returns each successful word and it's chemically-written equivalent. Used to generate chemical elements for [Alien Ink](https://www.vthunt.com/past-hunts/haunt-2023/tattos).
*This file also contains a pythonic list of all Virginia Tech buildings and additional Blacksburg businesses/buildings*

## doubletriples.py
Returns a list of words that contain a set of two (or more) triplicated letters.
For example: *abbreviatable, revitle, ['a', 'b']*

## fadjectives.py
Generates a list of all adjectives beginning with a given letter and removes (most) profanity. 

## nicholascagequestionmark.py
Generates a set of words such that taking a letter from each word spells out a given message, and the preceding letters of those words will spell out a second given message. Used in an earlier iteration of [Not-So-National Treasure](https://www.vthunt.com/past-hunts/hunt-2024/treasure). 

## TheBoggler.py
My pride and joy, and also the bane of my existence. Used to generate boggle boards for [Boggling The Mind](https://www.vthunt.com/past-hunts/hunt-2024/boggle) that meet the following requirements:
- Uses a given set of input words (feeders) with increasing lengths (3-8)
- Each feeder word must be laid out on the board so that is in the shape of a given letter
- The board must be arranged so that there is only one possible way to spell each feeder word

Also generates list of possible feeder words that, when arranged in order from shortest to longest, spell out BOLLOS with their first letters, and BOGGLE with their last, with lengths 3-8. Previous versions of the code included code to test different combinations of feeder words with the board generation code. This code has been commented out (the recursion to generate boards takes a really really long time, and every tested combination of feeders generates at least one board).

## universefile.py
Generates large text files with list of "Earths" 0-9999999, with facts about known universes filled, and "Uncharted" for all other universes. Was used for several different generations (the results of which are all included in the repository) including a logarithmicly grouped list, a list sorted in groups of 100 Earths, and one very long, non-grouped list (not included because it exceeds file size limit). Used to create filler file for Google Drive in [Rekam's Login](https://www.vthunt.com/past-hunts/hunt-2023/rekams-login). 

## words_states.py
Returns a list of words that can be created using only U.S. state abbreviations.

# Other included files:
## wordsDictionary.txt
List of 3731 English words with part of speech, definition, and link to dictionary.com page.

## words.txt
Big list of 466,550 English words.

## commonwords.txt
List of 10,000 most commonly used English words.

