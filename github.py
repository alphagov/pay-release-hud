#!/usr/bin/env python

import requests
import json
import re
import datetime
import os

from itertools import groupby
from enum import Enum 


headers = {'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN')}



# cache some things
object_cache = {}

def get_object_and_headers(url, cache = False, fallback = False):
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



class Repo:
  def __init__(self, org, name):
    self.org = org
    self.name = name
    
  def fetch_tags(self):
    tags = []
    tags_url = 'https://api.github.com/repos/%s/git/refs/tags?per_page=100' % str(self)
  
    while tags_url:
      (headers, content) = get_object_and_headers(tags_url, False, True)
      for ref in content:
        name = ref['ref']
        if name.startswith('refs/tags/'):
          tags.append(Tag(self, name[10:], ref['object']['url']))

      # # parse out github's weird pagination format
      tags_url = None
      if 'Link' in headers:
        links = map(lambda x: x.strip(), r.headers['Link'].split(','))
        for link in links:
          (url, rel) = link.split(';')
          if rel.strip() == 'rel="next"':
            url = url.strip()
            if url[0] == '<' and url[-1] == '>':
              tags_url = url[1:-1]
    
    return tags
    
  def __repr__(self):
    return 'Repo(%s)' % str(self)
    
  def __str__(self):
    return '%s/%s' % (self.org, self.name)
  
    
    
class TagType(Enum):
  UNKNOWN             = 0
  RELEASE_CREATED     = 1
  RELEASE_APPROVED    = 2
  STAGING_DEPLOYED    = 3
  STAGING_APPROVED    = 4
  PRODUCTION_DEPLOYED = 5
  
  

class Tag:
  def __init__(self, repo, name, url):
    self.repo = repo
    self.name = name
    self.url = url
    
    release_created_match = re.match('^alpha_release-([0-9]+)$', self.name)
    if release_created_match:
      self.release_num = int(release_created_match.group(1))
      self.type = TagType.RELEASE_CREATED
    else:    
      release_approved_match = re.match('^approved-alpha_release-([0-9]+)$', self.name)
      if release_approved_match:
        self.release_num = int(release_approved_match.group(1))
        self.type = TagType.RELEASE_APPROVED
      else:
        staging_deployed_match = re.match('^alpha_staging-[0-9]+-([0-9]+)$', self.name)
        if staging_deployed_match:
          self.release_num = int(staging_deployed_match.group(1))
          self.type = TagType.STAGING_DEPLOYED
        else:
          staging_approved_match = re.match('^approved-alpha_staging-[0-9]+-([0-9]+)$', self.name)
          if staging_approved_match:
            self.release_num = int(staging_approved_match.group(1))
            self.type = TagType.STAGING_APPROVED
          else:    
            production_deployed_match = re.match('^alpha_production-[0-9]+-([0-9]+)$', self.name)
            if production_deployed_match:
              self.release_num = int(production_deployed_match.group(1))
              self.type = TagType.PRODUCTION_DEPLOYED
            else:
              self.release_num = None
              self.type = TagType.UNKNOWN
            
    
  def get_details(self):
    return get_object(self.url, True)
    
  def get_commit(self):
    return get_object(self.get_details()['object']['url'], True)
    
  def get_html_url(self):
    return self.get_commit().get('html_url', '')
    
  def get_merge_date(self):
    return datetime.datetime.strptime(self.get_commit()['author']['date'], "%Y-%m-%dT%H:%M:%SZ")
    
  def get_feature_commit(self):
    feature_commit_url = self.get_commit()['parents'][1]['url'].replace('/git/', '/')
    return get_object(feature_commit_url, True)
    
  def get_feature_author(self):
    return self.get_feature_commit().get('committer', None)

  def __repr__(self):
    return "Tag(%s %s %s)" % (self.name, self.release_num, self.type)
  
  
    
class Release:
  def __init__(self, release_num, tags):
    self.release_num = release_num
    self.tags = tags
    self.repo = self.tags[0].repo
    self.stage = TagType(max(map(lambda tag: tag.type.value, tags)))

  def get_merge_date(self):
    return self.tags[0].get_merge_date()
    
  def get_feature_author(self):
    return self.tags[0].get_feature_author()
    
  def get_html_url(self):
    return self.tags[0].get_html_url()

  def __repr__(self):
    return "Release(%s %s %s)" % (self.repo, self.release_num, TagType(self.stage))



class Stages(Enum):
  RELEASE_CREATED     = 1
  RELEASE_APPROVED    = 2
  STAGING_DEPLOYED    = 3
  STAGING_APPROVED    = 4
  STAGING_PROMOTED    = 5
  PRODUCTION_BEHIND   = 6
  PRODUCTION_DEPLOYED = 7



def build_stages(repo):
  tags = sorted(filter(lambda tag: tag.type is not TagType.UNKNOWN, repo.fetch_tags()), key=lambda t : t.release_num)
  releases = []
  for release_num, tags in groupby(tags, lambda t: t.release_num):
    releases.append(Release(release_num, list(tags)))

  # pop relevant releases for each sequential stage
  stages = {}
      
  stages[Stages.RELEASE_CREATED] = []
  while releases and releases[-1].stage == TagType.RELEASE_CREATED:
    stages[Stages.RELEASE_CREATED].append(releases.pop())

  stages[Stages.RELEASE_APPROVED] = []
  while releases and releases[-1].stage == TagType.RELEASE_APPROVED:
    stages[Stages.RELEASE_APPROVED].append(releases.pop())

  stages[Stages.STAGING_DEPLOYED] = []
  while releases and releases[-1].stage == TagType.STAGING_DEPLOYED:
    stages[Stages.STAGING_DEPLOYED].append(releases.pop())

  stages[Stages.STAGING_APPROVED] = []
  while releases and releases[-1].stage == TagType.STAGING_APPROVED:
    stages[Stages.STAGING_APPROVED].append(releases.pop())

  stages[Stages.PRODUCTION_DEPLOYED] = []
  while releases and releases[-1].stage == TagType.PRODUCTION_DEPLOYED:
    stages[Stages.PRODUCTION_DEPLOYED].append(releases.pop())

  # only show the current version for what's deployed 
  if stages[Stages.STAGING_DEPLOYED]: 
    stages[Stages.STAGING_DEPLOYED] = stages[Stages.STAGING_DEPLOYED][0:1]
  
  if stages[Stages.PRODUCTION_DEPLOYED]:
    stages[Stages.PRODUCTION_DEPLOYED] = stages[Stages.PRODUCTION_DEPLOYED][0:1]

  # if nothing showing on staging pending list, staging must be on same version as production
  if not stages[Stages.STAGING_DEPLOYED] and not stages[Stages.STAGING_APPROVED]:
    stages[Stages.STAGING_PROMOTED] = stages[Stages.PRODUCTION_DEPLOYED]
  else:
    stages[Stages.STAGING_PROMOTED] = []
  
  # show production as needing update if there are staging releases approved for production
  if stages[Stages.STAGING_APPROVED]:
    stages[Stages.PRODUCTION_BEHIND] = stages[Stages.PRODUCTION_DEPLOYED]
    stages[Stages.PRODUCTION_DEPLOYED] = []
  else:
    stages[Stages.PRODUCTION_BEHIND] = []
    
  return stages