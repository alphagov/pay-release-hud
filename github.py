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
    parents = self.get_commit()['parents']
    if len(parents) > 1:
      feature_commit_url = parents[1]['url'].replace('/git/', '/')
      return get_object(feature_commit_url, True)
    else:
      return None
    
  def get_feature_author(self):
    feature_commit = self.get_feature_commit()
    if feature_commit:
      return feature_commit.get('committer', None)
    else:
      return {'login': '???'}

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



class Component:
  def __init__(self, repo):
    tags = sorted(filter(lambda tag: tag.type is not TagType.UNKNOWN, repo.fetch_tags()), key=lambda t : t.release_num)
    
    # build releases list, newest first
    releases = []
    for release_num, tags in groupby(tags, lambda t: t.release_num):
      releases.insert(0, Release(release_num, list(tags)))

    try:
      # find latest production deploy
      production_deployed = next(r for r in releases if r.stage == TagType.PRODUCTION_DEPLOYED)
      staging_release_num_cutoff = production_deployed.release_num
    except StopIteration:
      production_deployed = None
      staging_release_num_cutoff = -1
      
    try:
      # find latest staging release (only one)
      # it will either be in STAGING_APPROVED or STAGING_DEPLOYED
      staging_release = next(r for r in releases \
        if (r.release_num > staging_release_num_cutoff) and ((r.stage == TagType.STAGING_APPROVED) or (r.stage == TagType.STAGING_DEPLOYED)))
    
      # separate further in to stages
      self.staging_approved = staging_release if staging_release.stage == TagType.STAGING_APPROVED else None
      self.staging_deployed = staging_release if staging_release.stage == TagType.STAGING_DEPLOYED else None
      self.staging_promoted = None
      self.production_behind = production_deployed
      self.production_deployed = None
    
      release_num_cutoff = min(production_deployed.release_num, staging_release.release_num)
    except StopIteration:
      # no staging release so staging must be same as production
      self.staging_approved = None
      self.staging_deployed = None
      self.staging_promoted = production_release
      self.production_behind = None
      self.production_deployed = production_release
      
      release_num_cutoff = production_release.release_num

  
    # get all created and approved releases, but don't bother showing anything below staging version
    # get releases and approved releases, but don't bother showing anything below staging's current version
    self.releases_created = list(filter(lambda r : (r.release_num > release_cutoff) and (r.stage == TagType.RELEASE_CREATED), releases))
    self.releases_approved = list(filter(lambda r : (r.release_num > release_cutoff) and (r.stage == TagType.RELEASE_APPROVED), releases))



def build_stages(repo):
  tags = sorted(filter(lambda tag: tag.type is not TagType.UNKNOWN, repo.fetch_tags()), key=lambda t : t.release_num)
  releases = []
  # build releases list, newest first
  for release_num, tags in groupby(tags, lambda t: t.release_num):
    releases.insert(0, Release(release_num, list(tags)))
  
  # pop relevant releases for each sequential stage
  stages = {}

  try:
    production_release = next(r for r in releases if r.stage == TagType.PRODUCTION_DEPLOYED)
  except StopIteration:
    production_release = None
  
  # there will only be one release on staging, find it
  try:
    staging_release = next(r for r in releases \
      if (production_release is None or (r.release_num > production_release.release_num)) and 
      ((r.stage == TagType.STAGING_APPROVED) or (r.stage == TagType.STAGING_DEPLOYED)))
      
    stages[Stages.STAGING_APPROVED] = [staging_release] if staging_release.stage == TagType.STAGING_APPROVED else []
    stages[Stages.STAGING_DEPLOYED] = [staging_release] if staging_release.stage == TagType.STAGING_DEPLOYED else []
    stages[Stages.STAGING_PROMOTED] = []
    stages[Stages.PRODUCTION_BEHIND] = [production_release] if production_release else []
    stages[Stages.PRODUCTION_DEPLOYED] = []
  except StopIteration:
    staging_release = production_release
        
    stages[Stages.STAGING_APPROVED] = []
    stages[Stages.STAGING_DEPLOYED] = []
    stages[Stages.STAGING_PROMOTED] = [production_release] if production_release else []
    stages[Stages.PRODUCTION_BEHIND] = []
    stages[Stages.PRODUCTION_DEPLOYED] = [production_release] if production_release else []
  
  ignore_before = staging_release.release_num
  
  # get all created and approved releases, but don't bother showing anything below staging version
  # get releases and approved releases, but don't bother showing anything below staging's current version
  stages[Stages.RELEASE_CREATED] = list(filter(lambda r : (r.release_num > ignore_before) and (r.stage == TagType.RELEASE_CREATED), releases))
  stages[Stages.RELEASE_APPROVED] = list(filter(lambda r : (r.release_num > ignore_before) and (r.stage == TagType.RELEASE_APPROVED), releases))
    
  return stages