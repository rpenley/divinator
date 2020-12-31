#!/bin/python
###########################################
# The all powerful and all flawed Divinator
# Will prognosticate for anyone or anything
# Free to use for your pleasure...  or pain 
###########################################

#Library imports
import datetime, time
from nltk.corpus import wordnet as wn
from random import sample

#input name (username not actual name)
#<name>
#
username = input("Enter your name: ")

# Get birthday and convert to unix time
birthstring = input("Enter your birthday in mm/dd/yy format: ")
birthstamp = time.mktime(datetime.datetime.strptime(birthstring, "%m/%d/%y").timetuple())

#randomly ask for extra input
#

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

print ("your name is " + username + " and your birthday is " + birthday)
