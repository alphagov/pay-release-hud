#!/usr/bin/env python

from flask import Flask, redirect, render_template, url_for, request
import os
import requests
import json
import re
import collections

app = Flask(__name__)

headers = {'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN')}



class Tag:
  def __init__(self, name, url):
    self.name = name
    self.url = url


def get_tag_detail(url):
  r = requests.get(url, headers=headers)
  print r.json()


def get_tag_refs(org, repo):
  tags = []
  tags_url = 'https://api.github.com/repos/%s/%s/git/refs/tags?per_page=100' % (org, repo)
  
  while tags_url:
    r = requests.get(tags_url, headers=headers)

    for ref in r.json():
      name = ref['ref']
      if name.startswith('refs/tags/'):
        tags += [Tag(name[10:], ref['object']['url'])]

    # # parse out github's weird pagination format
    tags_url = None
    if 'Link' in r.headers:
      links = map(lambda x: x.strip(), r.headers['Link'].split(','))
      for link in links:
        (url, rel) = link.split(';')
        if rel.strip() == 'rel="next"':
          url = url.strip()
          if url[0] == '<' and url[-1] == '>':
            tags_url = url[1:-1]

  return tags
  
    
class Stage:
  def __init__(self, repo, release):
    self.repo = repo
    self.release = release
    self.released = False
    self.staging_approved = False
    self.staging_deployed = False
    self.production_approved = False
    self.production_deployed = False
      
  def __repr__(self):
    return "Stage(%s %s [%s %s %s %s])" % \
      (self.repo, self.release, self.staging_approved, self.staging_deployed, self.production_approved, self.production_deployed)

  
  
def get_stages(org, repo):
  tags = get_tag_refs(org, repo)
  stages = {}
  for tag in tags:
    number = None
    
    released = re.match('^alpha_release-([0-9]+)$', tag.name)
    if released:
      number = int(released.group(1))
      
    staging_approved = re.match('^approved-alpha_release-([0-9]+)$', tag.name)
    if staging_approved:
      number = int(staging_approved.group(1))
    
    staging_deployed = re.match('^alpha_staging-[0-9]+-([0-9]+)$', tag.name)
    if staging_deployed:
      number = int(staging_deployed.group(1))
      
    production_approved = re.match('^approved-alpha_staging-[0-9]+-([0-9]+)$', tag.name)
    if production_approved:
      number = int(production_approved.group(1))
      
    production_deployed = re.match('^alpha_production-[0-9]+-([0-9]+)$', tag.name)
    if production_deployed:
      number = int(production_deployed.group(1))
    
    if number:
      if number in stages:
        stage = stages[number]
      else:
        stage = Stage(repo, number)
        stages[number] = stage
    
      stage.released = stage.released or bool(released)
      stage.staging_approved = stage.staging_approved or bool(staging_approved)
      stage.staging_deployed = stage.staging_deployed or bool(staging_deployed)
      stage.production_approved = stage.production_approved or bool(production_approved)
      stage.production_deployed = stage.production_deployed or bool(production_deployed)
    
  def cmp_stages(a, b):
      if a.release < b.release:
          return 1
      elif a.release == b.release:
          return 0
      else:
          return -1
    
  return sorted(stages.values(), cmp = cmp_stages)



def split_stages(stages):
  production_releases = filter(lambda release: release.production_deployed, stages)
  production_latest = production_releases[0] if len(production_releases) > 0 else None
  
  staging_releases = filter(lambda release: release.staging_deployed \
    and ((production_latest is None) or (release.release >= production_latest.release)), \
    stages)
  staging_latest = staging_releases[0] if len(staging_releases) > 0 else None
  
  other_releases = filter(lambda release: not release.staging_deployed and not release.production_deployed \
    and ((production_latest is None) or (release.release > production_latest.release)) \
    and ((staging_latest is None) or (release.release > staging_latest.release)), \
    stages)
    
  return (production_latest, staging_latest, other_releases)


@app.route('/')
def start():
  production = []
  staging = []
  releases = []
  
  for repo in ('pay-connector', 'pay-selfservice', 'pay-frontend', 'pay-publicapi', 'pay-cardid', 'pay-publicauth', 'pay-logger'):
    (production_release, staging_release, other_releases) = split_stages(get_stages('alphagov', repo))
    if production_release: production += [production_release]
    if staging_release: staging += [staging_release]
    releases += other_releases
  
  return render_template('index.html', production = production, staging = staging, releases = releases)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    