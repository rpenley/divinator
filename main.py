#!/bin/python
###########################################
# The all powerful and all flawed Divinator
# Will prognosticate for anyone or anything
# Free to use for your pleasure...  or pain 
###########################################

# Library imports and Downloads
import datetime, random, textwrap, markovify, nltk
from nltk.corpus import wordnet as wn

### Verify reference texts are downloaded
try:
	nltk.data.find('corpus/wordnet')
	nltk.data.find('corpus/gutenberg')
	nltk.data.find('corpus/genesis')
	nltk.data.find('tokenizers/punkt')
except LookupError:
	nltk.download('wordnet', quiet=True)
	nltk.download('gutenberg', quiet=True)
	nltk.download('punkt', quiet=True)
	nltk.download('genesis', quiet=True)
### Input name (username not actual name)
#
#username = input("Enter your name: ")

### Get birthday and convert to unix time
#birthstring = input("Enter your birthday in mm/dd/yy format: ")
#birthstamp = time.mktime(datetime.datetime.strptime(birthstring, "%m/%d/%y").timetuple())

### Randomly ask for extra input
#
#for synset in list(wn.all_synsets('n')):
#print(sample(wn.all_synsets('n'),1))
#nouns = wn.all_synsets('n')
#print(type(nouns))

#bible = nltk.Text(nltk.corpus.gutenberg.sents(u'bible-kjv.txt'))
#bibleText = nltk.Text(bible)
#bibleText.generate()

#cfd = nltk.ConditionalFreqDist(nltk.bigrams(bible))
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams) 
#generate_model(cfd, 'noah')

def generate_sents(corpus_file, n=1):
    words = nltk.corpus.gutenberg.words(corpus_file)
    fd = nltk.FreqDist(words)
    sents = nltk.corpus.gutenberg.sents(corpus_file)
    ss= sorted(sents, reverse=True, key=(lambda x:sum(fd[w] for w in x)) )
    for i in range(n):
        for line in ' '.join(ss[i]):
            print(line, end='')

generate_sents('austen-emma.txt', 69)
# Pick a random word from the corpus to start with
#is_noun = lambda pos: pos[:2] == 'NN'
#tokenized = nltk.word_tokenize(bible)
#nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
#print(random.choice(bible))
#word = random.choice(bible)
#print ("and behold the lord said " + word)
# generate 15 more words
#for i in range(15):
#    print(word, end=' ')
#    if word in cfd:
#        word = random.choice(list(cfd[word].keys()))
#    else:
#        break

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
