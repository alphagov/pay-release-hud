#!/usr/bin/env python

import requests
import json
import re
import datetime
import os

from itertools import groupby
from enum import Enum 

import testing


HEADERS = {'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN')}
DEV_MODE = os.environ.get('DEV_MODE') == 'true'


# cache some things
OBJECT_CACHE = {}

def get_object_and_headers(url, cache = False, fallback = False):
  if DEV_MODE:
    return testing.get_object_and_headers(url)
  
  if cache and (url in OBJECT_CACHE):
    return object_cache[url]

  r = requests.get(url, headers=HEADERS)
  if r.status_code < 400:
    object = (r.headers, r.json())
    OBJECT_CACHE[url] = object
    return object
  elif fallback:
    if cache and (url in OBJECT_CACHE):
      return object_cache[url]
    else:
      r.raise_for_status()
  else:
    r.raise_for_status()
  


def get_object(url, cache = False):
  return get_object_and_headers(url, cache)[1]
