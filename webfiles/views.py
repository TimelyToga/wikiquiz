__author__ = 'Tim'
try: import simplejson as json
except ImportError: import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from webfiles import lang
from bs4 import BeautifulSoup

import re

def home(request):
  template = loader.get_template('index.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))

def quiz(request, wiki_title):
  ## title
  article_title = wiki_title.replace("_", " ")

  ## Question generation
  article_text = lang.get_text(wiki_title=wiki_title)
  #  Infinite internal linking
  article_text = re.sub(r"https:\/\/en.wikipedia.org\/wiki\/", "", article_text)
  questions_text = BeautifulSoup(article_text).get_text()
  questions_text = re.sub("\[\d{0,3}\]", "", questions_text).strip()
  corpus_qs = lang.questions(questions_text)
  vcard_qs = lang.get_vcard(wiki_title=wiki_title)
  total_qs = corpus_qs + vcard_qs


  ## TEMPLATE
  template = loader.get_template('quiz.html')
  context = RequestContext(request, {"wiki_text": article_text, "article_title": article_title, "questions": total_qs})
  return HttpResponse(template.render(context))

def test(request, wiki_title):
  article_title = wiki_title.replace("_", " ")

  ## Basic shit
  article_text = lang.get_text(wiki_title=wiki_title)
  article_text = re.sub(r"https:\/\/en.wikipedia.org\/wiki\/", "", article_text)
  questions_text = BeautifulSoup(article_text).get_text()
  questions_text = re.sub("\[\d{0,3}\]", "", questions_text).strip()
  sentence_list = lang.get_sentences(questions_text)

  ## Template rendering
  template = loader.get_template('test.html')
  context = RequestContext(request, {"article_title": article_title, "sentence_list": sentence_list})
  return HttpResponse(template.render(context))