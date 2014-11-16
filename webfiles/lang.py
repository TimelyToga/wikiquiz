__author__ = 'Tim'
import nltk
import string

from collections import Counter
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from wikiquiz import settings

import random


def get_tokens(text):
  text = BeautifulSoup(text).get_text()
  lowers = text.lower()
  no_punctuation = lowers.translate(None, string.punctuation)
  tokens = nltk.word_tokenize(no_punctuation)
  filtered = [w for w in tokens if not w in stopwords.words('english')]

  count = Counter(tokens)

  return tokens

def questions(text):
  question_list = []
  sentences = sent_tokenize(text)

  ## Only sentences of sufficient length
  valid_sentences = []
  for s in sentences:
    if(len(s) > settings.MIN_SENT_LENGTH):
      valid_sentences.append(s)

  for i in range(0, 5):
    question_list.append(random.choice(valid_sentences))

  return question_list


def get_text(wiki_title="Jabari_Parker"):
  from readability import ParserClient
  parser_client = ParserClient(settings.PARSER_TOKEN)
  parser_response_text = parser_client.get_article_content(settings.WIKI_URL + wiki_title).content['content'].replace("\n", " ")
  text = BeautifulSoup(parser_response_text).get_text()
  text = text.replace("/<img[^>]*>/g","")
  return text.split('<span class="mw-headline" id="References"')[0]

