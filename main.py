#!/usr/bin/env python

from flask import Flask, render_template
import os, sys, traceback

from releases import *

app = Flask(__name__)


@app.route('/')
def start():
  try:
    components = []
    for repo in ('pay-frontend', 'pay-selfservice', 'pay-connector', 'pay-publicapi', 'pay-cardid', 'pay-publicauth', 'pay-logger', 'pay-adminusers'):
      components.append(Component(Repo('alphagov', repo)))
    
    components_behind = 0
    for component in components:
      if component.production_behind:
        components_behind += 1
  
    return render_template('index.html', components = components, components_behind = components_behind, TagType=TagType)
  except:
    exc_info = sys.exc_info()
    print "Unexpected error:", exc_info
    traceback.print_exception(*exc_info)
    return render_template('error.html')



if __name__ == '__main__':
  dev_mode = os.environ.get('DEV_MODE') == 'true'
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=dev_mode)
