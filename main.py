#!/usr/bin/env python

from flask import Flask, render_template
from github import *
import os, sys, traceback

app = Flask(__name__)


@app.route('/')
def start():
  try:
    stages = []
    for repo in ('pay-selfservice', 'pay-connector', 'pay-frontend', 'pay-publicapi', 'pay-cardid', 'pay-publicauth', 'pay-logger'):
      stages.append(build_stages(Repo('alphagov', repo)))
    
    # add over list items
    stages_all = reduce(lambda x, y: dict((k, v + y[k]) for k, v in x.iteritems()), stages)
  
    # sort by date. oldest at the top.
    for stage, releases in stages_all.items():
      stages_all[stage] = sorted(releases, key=lambda r: r.get_merge_date())
  
    return render_template('index.html', stages = stages_all, Stages = Stages)
  except:
    print "Unexpected error:", sys.exc_info()[0]
    traceback.print_exc()
    return render_template('error.html')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
