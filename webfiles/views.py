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
  from readability import ParserClient
  parser_client = ParserClient(settings.PARSER_TOKEN)
  parser_response_text = parser_client.get_article_content(settings.WIKI_URL + wiki_title).content['content'].replace("\n", " ")

  ## Clean article
  #  Remove References
  cleaned_text = parser_response_text.replace("/<img[^>]*>/g","")
  cleaned_text = cleaned_text.split('<span class="mw-headline" id="References"')[0]

  # Create Plain Text Version
  # lang.get_tokens(cleaned_text)

  ## title
  article_title = wiki_title.replace("_", " ")

  questions = lang.questions()

  ## TEMPLATE
  template = loader.get_template('quiz.html')
  context = RequestContext(request, {"wiki_text": cleaned_text, "article_title": article_title, "questions": questions})
  return HttpResponse(template.render(context))




