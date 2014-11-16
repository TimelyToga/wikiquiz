__author__ = 'Tim'
try: import simplejson as json
except ImportError: import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext, loader

import requests
import logging

