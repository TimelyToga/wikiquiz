__author__ = 'Tim'
import nltk
import string

from collections import Counter
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


def get_tokens(text):
  text = BeautifulSoup(text).get_text()
  lowers = text.lower()
  no_punctuation = lowers.translate(None, string.punctuation)
  tokens = nltk.word_tokenize(no_punctuation)
  filtered = [w for w in tokens if not w in stopwords.words('english')]

  count = Counter(tokens)

  return tokens