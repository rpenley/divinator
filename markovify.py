#!/usr/bin/python

import markovify
import pandas as pd
import urllib3
from bs4 import BeautifulSoup as bs
http = urllib3.PoolManager()

url = 'http://www.gutenberg.org/files/10/10.txt'
response = http.request('GET', url)
kjv = pd.read_fwf(bs(response.data))
kjv.head(3)
text_model = markovify.NewlineText(kjv.headline_text, state_size = 2)
# Print ten randomly-generated sentences using the built model
for i in range(10):
    print(text_model.make_sentence())
