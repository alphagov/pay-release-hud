#!/usr/bin/env python

import requests
import json
import re
import datetime
import os

from itertools import groupby
from enum import Enum 

from github import *



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
  STAGING_DEPLOYED    = 2
  PRODUCTION_DEPLOYED = 3
  
  

class Tag:
  def __init__(self, repo, name, url):
    self.repo = repo
    self.name = name
    self.url = url
    self.merge_date = None;
    
    release_created_match = re.match('^alpha_release-([0-9]+)$', self.name)
    if release_created_match:
      self.release_num = int(release_created_match.group(1))
      self.type = TagType.RELEASE_CREATED
    else:    
      staging_deployed_match = re.match('^alpha_staging-[0-9]+-([0-9]+)$', self.name)
      if staging_deployed_match:
        self.release_num = int(staging_deployed_match.group(1))
        self.type = TagType.STAGING_DEPLOYED
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
    if not self.merge_date:
      self.merge_date = datetime.datetime.strptime(self.get_commit()['author']['date'], "%Y-%m-%dT%H:%M:%SZ")

    return self.merge_date
    
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
      author = feature_commit.get('author')
      if author:
        return author
        
      committer = feature_commit.get('committer')
      if committer:
        return committer
    
    return {'login': '?'}

  def __repr__(self):
    return "Tag(%s %s %s)" % (self.name, self.release_num, self.type)
  
  
    
class Release:
  def __init__(self, release_num, tags):
    self.release_num = release_num
    self.tags = tags
    self.repo = self.tags[0].repo
    self.stage = TagType(max(map(lambda tag: tag.type.value, tags)))
    self.is_duplicate = False

  def get_merge_date(self):
    return self.tags[0].get_merge_date()
    
  def get_feature_author(self):
    return self.tags[0].get_feature_author()
    
  def get_html_url(self):
    return self.tags[0].get_html_url()

  def set_duplicate(self):
    self.is_duplicate = True

  def __repr__(self):
    return "Release(%s %s %s)" % (self.repo, self.release_num, TagType(self.stage))



class Component:
  def __init__(self, repo):
    self.repo = repo
    
    tags = sorted(filter(lambda tag: tag.type is not TagType.UNKNOWN, repo.fetch_tags()), key=lambda t : t.release_num)
    
    # build releases list, newest first
    releases = []
    for release_num, tags in groupby(tags, lambda t: t.release_num):
      tag_list = list(tags)
      release = Release(release_num, tag_list)
      releases.insert(0, release)

    try:
      # find latest production deploy
      production_deployed = next(r for r in releases if r.stage == TagType.PRODUCTION_DEPLOYED)
      staging_release_num_cutoff = production_deployed.release_num
    except StopIteration:
      production_deployed = None
      staging_release_num_cutoff = -1
      
    try:
      # find latest staging release (only one)
      staging_release = next(r for r in releases \
        if (r.release_num > staging_release_num_cutoff) and (r.stage == TagType.STAGING_DEPLOYED))
    
      # separate further in to stages
      self.staging_deployed = staging_release # if staging_release.stage == TagType.STAGING_DEPLOYED else None
      self.staging_promoted = None
      self.production_behind = production_deployed
      self.production_deployed = None
    
      release_num_cutoff = max(production_deployed.release_num, staging_release.release_num)
    except StopIteration:
      # no staging release so staging must be same as production
      self.staging_deployed = None
      self.staging_promoted = production_deployed
      self.production_behind = None
      self.production_deployed = production_deployed
      
      release_num_cutoff = staging_release_num_cutoff
  
    # identify release duplicates by comparing all pairs upt to and including current staging deploy
    duplicate_candiates = list(filter(lambda r : (r.release_num >= release_num_cutoff), releases))
    for release, prev in zip(duplicate_candiates, duplicate_candiates[1:]):
      if release.tags[0].get_merge_date()  == prev.tags[0].get_merge_date():
        release.set_duplicate()

    self.releases = list(filter(lambda r : (r.release_num > release_num_cutoff) and \
       (r.stage == TagType.RELEASE_CREATED), releases))

    # sort ascending releases
    self.releases.sort(key=lambda r: r.release_num)
