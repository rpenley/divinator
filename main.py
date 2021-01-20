#!/bin/python
###########################################
# The all powerful and all flawed Divinator
# Will prognosticate for anyone or anything
# Free to use for your pleasure...  or pain 
###########################################

# Library imports and Downloads
#!/usr/bin/python
import random
import markovify
import re
import spacy

# Load the spaCy English model
nlp = spacy.load("en")

# Replace the word_split and word_join methods in markovify with spaCy models, as shown in the markovify demo
class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

# Load bible data (King James Version)
kjv = open("data/kjv.txt").read()
kjvmodel = markovify.Text(kjv)

# Load the kjv text
kjv = open("data/kjv.txt").read()
kjvmodel = markovify.Text(kjv)

# Load the kjv text
kjv = open("data/kjv.txt").read()
kjvmodel = markovify.Text(kjv)

# Load the kjv text
kjv = open("data/kjv.txt").read()
kjvmodel = markovify.Text(kjv)

# Load the kjv text
kjv = open("data/kjv.txt").read()
kjvmodel = markovify.Text(kjv)

# Feel free to play with the parameters of the combined model, but 1:1.7 seems to work ok empirically
#kjvicomodel = markovify.combine([ kjvmodel, icomodel ], [ 1, 1.7 ])

#for i in range(96):
print(kjvmodel.make_short_sentence(280))

### Input name (username not actual name)
#
#username = input("Enter your name: ")

### Get birthday and convert to unix time
#birthstring = input("Enter your birthday in mm/dd/yy format: ")
#birthstamp = time.mktime(datetime.datetime.strptime(birthstring, "%m/%d/%y").timetuple())

### Randomly ask for extra input
#

### Nostradamus 
#

### Star Data
#

### Randomly ask yes or no question?
#

### Fake calculating screen
#

### Low quality picture
#

### Present a birthday number (vision? sequence? significance?)
#

### Present birthday letter
#

### Present a bad nlp joke or recipe
#

### Present a good constellation and a bad constellation
#

### Generate a horroscope (this year do..., this year avoid)
#

### Generate a music thing?
#

### Present a picture
#

