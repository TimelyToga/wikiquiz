__author__ = 'Tim'
import nltk
import string

from collections import Counter
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from wikiquiz import settings

import random
import requests
import re

templates = {r"\S{0,20}ed in \d{4}": 0,  ## {past tense verb} in {year}
             r"(?:\s*\b([A-Z][A-Za-z]+)\b){1,2} was born on (\d{1,3}.{0,3} \S{3,10}|\S{3,10} \d{1,3}.{0,3}) \d{4}": 1, ## {Proper Noun} was born on {Month} {Day}, {Year}
            }

vcard_qs = {"Born": {"id": 0, "question": "When and where was %s born?"},
            "Population": {"id": 1, "question":"What is the population of %s?"},
            "Predecessor": {"id": 2, "question":"Who was %s's predecessor?"},
            "Year founded": {"id": 3, "question": "When was %s founded?"},
            "Founded": {"id": 4, "question": "When was %s founded?"},
            "Molecular formula": {"id": 5, "question": "What is the chemical formula for %s?"},
            "Density": {"id": 6, "question": "What is the density of %s?"}}


def questions(text):
  ## Sentences
  valid_sentences = get_sentences(text)

  template_matches = {}
  final_question_list = []
  cur_q = 0

  ## Find and record template matches
  for s in valid_sentences:
    for t in templates.keys():
        r = re.search(t, s)
        if r is not None:
          template_matches[s] = {"id": templates[t], "chunk": r.group(0)}

  ## Render the Questions and Answers
  for entry in template_matches.keys():
    id = template_matches[entry]['id']
    chunk = template_matches[entry]['chunk']
    if id == 0:
      ## Handle past tense year
      split = chunk.split(" in ")
      q_text = " " + split[0] + " in what year?"
      year = split[1]
      final_q_text = entry.split(chunk)[0] + q_text
      final_question_list.append({"question":final_q_text, "answer": year, "num": cur_q})
      cur_q += 1
    elif id == 1:
      ## Handle born in
      split = chunk.split(" was born on ")
      name = split[0].strip()
      q_text = "When was " + name + " born?"
      answer = split[1]
      final_question_list.append({"question": q_text, "answer":answer, "num": cur_q})
      cur_q += 1
    else:
      ## Handle broken
      print "We fucked up, bitch"

  return final_question_list

def get_sentences(text):
  sentences = sent_tokenize(text)

  ## Only sentences of sufficient length
  valid_sentences = []
  for s in sentences:
    if(len(s) > settings.MIN_SENT_LENGTH):
      valid_sentences.append(s)
  return valid_sentences


def get_text(wiki_title="Jabari_Parker"):
  from readability import ParserClient
  parser_client = ParserClient(settings.PARSER_TOKEN)
  parser_response_text = parser_client.get_article_content(settings.WIKI_URL + wiki_title).content['content'].replace("\n", " ")
  text = parser_response_text.replace("/<img[^>]*>/g","")
  text = text.split('<span class="mw-headline" id="See_also"')[0]
  text = text.split('<span class="mw-headline" id="Notes"')[0]
  text = text.split('<span class="mw-headline" id="References"')[0]
  text = text.split('<span class="mw-headline" id="Notes_and_references"')[0]
  return text

def get_vcard(wiki_title="Jabari_Parker"):
  url = settings.WIKI_URL + wiki_title
  html = requests.get(url).content

  article_title = wiki_title.replace("_", " ")

  vcard_results = {}
  final_question_list = []
  cur_q = 100

  ## Create soup
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html)
  try:
    vcard = soup.findAll(attrs={'class': re.compile(r".*\bvcard\b.*")})[0]
  except IndexError:
    try:
      vcard = soup.findAll(attrs={'class': re.compile(r".*\binfobox\b.*")})[0]
    except IndexError:
      return []
  ths = vcard.findAll("th")

  ## Look for vcard questions
  for q in vcard_qs.keys():
    id = vcard_qs[q]["id"]
    question = vcard_qs[q]["question"] % article_title
    for i in ths:
      if i.string == q:
        ## Extract information and render question
        try:
          answer = i.parent.td.get_text()
        except AttributeError:
          answer = i.parent.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        answer = re.sub(r'\[.+?\]\s*', ' ', answer)
        final_question_list.append({"id": id, "question": question, "answer": answer, "num": cur_q })
        cur_q += 1

  return final_question_list


