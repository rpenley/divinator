#!/bin/python
###########################################
# The all powerful and all flawed Divinator
# Will prognosticate for anyone or anything
# Free to use for your pleasure...  or pain 
###########################################

# Library imports and Downloads
import datetime, nltk, random
from nltk.corpus import wordnet as wn
nltk.download('wordnet', quiet=True)
nltk.download('gutenberg', quiet=True)
nltk.download('punkt', quiet=True)
#input name (username not actual name)
#<name>
#
#username = input("Enter your name: ")

# Get birthday and convert to unix time
#birthstring = input("Enter your birthday in mm/dd/yy format: ")
#birthstamp = time.mktime(datetime.datetime.strptime(birthstring, "%m/%d/%y").timetuple())

#randomly ask for extra input
#
#for synset in list(wn.all_synsets('n')):
#print(sample(wn.all_synsets('n'),1))
nouns = wn.all_synsets('n')
print(type(nouns))

bible = nltk.corpus.gutenberg.words(u'bible-kjv.txt')
#bibleText = nltk.Text(bible)
#bibleText.generate()

# NLTK shortcuts :)
cfd = nltk.ConditionalFreqDist(nltk.bigrams(bible))

# pick a random word from the corpus to start with
word = random.choice(bible)
# generate 15 more words
for i in range(15):
    print(word, end=' ')
    if word in cfd:
        word = random.choice(list(cfd[word].keys()))
    else:
        break

#randomly ask yes or no question?
#

#fake calculating screen
#

#low quality picture
#

#present a birthday number (vision? sequence? significance?)
#

#present birthday letter
#

#present a bad nlp joke or recipe
#

#present a good constellation and a bad constellation
#

#generate a horroscope (this year do..., this year avoid)
#

#generate a music thing?
#

#present a picture
