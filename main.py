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
  def __init__(self, repo, name, url):
    self.repo = repo
    self.name = name
    self.url = url
    
  def get_details(self):
    return requests.get(self.url, headers=headers).json()



def get_tag_refs(org, repo):
  tags = []
  tags_url = 'https://api.github.com/repos/%s/%s/git/refs/tags?per_page=100' % (org, repo)
  
  while tags_url:
    r = requests.get(tags_url, headers=headers)

    for ref in r.json():
      name = ref['ref']
      if name.startswith('refs/tags/'):
        tags += [Tag(repo, name[10:], ref['object']['url'])]

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
  
    
    
class Release:
  def __init__(self, repo, release):
    self.repo = repo
    self.release = release
    self.released = False
    self.staging_approved = False
    self.staging_deployed = False
    self.production_approved = False
    self.production_deployed = False
      
  def __repr__(self):
    return "Release(%s %s [%s %s %s %s %s])" % \
      (self.repo, self.release, self.staging_approved, self.staging_deployed, self.production_approved, self.production_deployed, self.deploy_behind)

  
  
def get_releases(org, repo):
  tags = get_tag_refs(org, repo)
  releases = {}
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
      if number in releases:
        release = releases[number]
      else:
        release = Release(repo, number)
        releases[number] = release
    
      release.released = release.released or bool(released)
      release.staging_approved = release.staging_approved or bool(staging_approved)
      release.staging_deployed = release.staging_deployed or bool(staging_deployed)
      release.production_approved = release.production_approved or bool(production_approved)
      release.production_deployed = release.production_deployed or bool(production_deployed)
  
  # fetch extra details about releases to be displayed
  
  def cmp_releases(a, b):
      if a.release < b.release:
          return 1
      elif a.release == b.release:
          return 0
      else:
          return -1
    
  return sorted(releases.values(), cmp = cmp_releases)



def split_releases(releases):
  production_history = filter(lambda release: release.production_deployed, releases)
  production_current = production_history[0] if len(production_history) > 0 else None
  production_uptodate = production_current
  
  staging_history = filter(lambda release: release.staging_deployed \
     and ((production_current is None) or (release.release >= production_current.release)), \
     releases)
     
  staging_current = staging_history[0] if len(staging_history) > 0 else None
  
  if not staging_current:
    staging_promoted = None
    staging_approved = None
    staging_awaiting = None
    production_update = None
  elif not production_current or staging_current.release != production_current.release:
    staging_promoted = None
    if staging_current.production_approved:
      staging_approved = staging_current
      staging_awaiting = None
    else:
      staging_approved = None
      staging_awaiting = staging_current
    production_update = production_current
    production_uptodate = None
  else:
    staging_promoted = staging_current
    staging_approved = None
    staging_awaiting = None
    production_update = None
     
  releases = filter(lambda release: not release.staging_deployed and not release.production_deployed \
    and ((production_current is None) or (release.release > production_current.release)) \
    and ((staging_current is None) or (release.release > staging_current.release)), \
    releases)
    
  releases_approved = filter(lambda release: release.staging_approved, releases)
  releases_new = filter(lambda release: not release.staging_approved, releases)
    
  return (
    [production_uptodate] if production_uptodate else [], 
    [production_update] if production_update else [], 
    [staging_promoted] if staging_promoted else [], 
    [staging_approved] if staging_approved else [], 
    [staging_awaiting] if staging_awaiting else [], 
    releases_approved, 
    releases_new
  )


@app.route('/')
def start():
  production_current = []
  production_update = []
  staging_promoted = []
  staging_approved = []
  staging_awaiting = []
  release_approved = []
  release_new = []
  
  for repo in ('pay-connector', 'pay-selfservice', 'pay-frontend', 'pay-publicapi', 'pay-cardid', 'pay-publicauth', 'pay-logger'):
    (repo_production_current,
      repo_production_update,
      repo_staging_promoted,
      repo_staging_approved,
      repo_staging_awaiting,
      repo_release_approved,
      repo_release_new) = split_releases(get_releases('alphagov', repo))
  
    production_current += repo_production_current
    production_update += repo_production_update
    staging_promoted += repo_staging_promoted
    staging_approved += repo_staging_approved
    staging_awaiting += repo_staging_awaiting
    release_approved += repo_release_approved
    release_new += repo_release_new
  
  return render_template('index.html', 
    production_current = production_current,
    production_update = production_update,
    staging_promoted = staging_promoted,
    staging_approved = staging_approved,
    staging_awaiting = staging_awaiting,
    release_approved = release_approved,
    release_new = release_new
  )



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    