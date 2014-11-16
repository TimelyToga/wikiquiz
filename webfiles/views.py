__author__ = 'Tim'
try: import simplejson as json
except ImportError: import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
from webfiles import lang
from bs4 import BeautifulSoup

import logging
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
  questions_text = BeautifulSoup(article_text).get_text()
  questions_text = re.sub("\[\d{0,3}\]", "", questions_text).strip()
  questions = lang.questions(questions_text)

  ## TEMPLATE
  template = loader.get_template('quiz.html')
  context = RequestContext(request, {"wiki_text": article_text, "article_title": article_title, "questions": questions})
  return HttpResponse(template.render(context))




