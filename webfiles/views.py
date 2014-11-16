__author__ = 'Tim'
try: import simplejson as json
except ImportError: import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader
import wikiquiz.settings as settings
from nltk.tokenize import word_tokenize
from webfiles import lang
import logging

def home(request):
  template = loader.get_template('index.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))

def quiz(request, wiki_title):
  ## title
  article_title = wiki_title.replace("_", " ")

  ## Question generation
  article_text = lang.get_text(wiki_title=wiki_title)
  questions = lang.questions(article_text)

  ## TEMPLATE
  template = loader.get_template('quiz.html')
  context = RequestContext(request, {"wiki_text": article_text, "article_title": article_title, "questions": questions})
  return HttpResponse(template.render(context))




