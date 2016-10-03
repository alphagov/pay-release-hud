#!/usr/bin/env python

import requests
import json
import re
import datetime
import os

from itertools import groupby
from enum import Enum 

import testing


headers = {'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN')}



# cache some things
object_cache = {}

def get_object_and_headers(url, cache = False, fallback = False):
  # return testing.get_object_and_headers(url)
  
  if cache and (url in object_cache):
    return object_cache[url]

  r = requests.get(url, headers=headers)
  if r.status_code < 400:
    object = (r.headers, r.json())
    object_cache[url] = object
    return object
  elif fallback:
    if cache and (url in object_cache):
      return object_cache[url]
    else:
      r.raise_for_status()
  else:
    r.raise_for_status()
  


def get_object(url, cache = False):
  return get_object_and_headers(url, cache)[1]
