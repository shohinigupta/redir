import os
from flask import Flask, redirect
from collections import defaultdict

SERVER_NAME = 'drf.vc'
REDIRS = defaultdict(lambda: 'https://www.{}'.format(SERVER_NAME), {
  'join': 'https://medium.com/@dormroomfund/join-the-dorm-room-fund-team-9a01f8326401',
  'join-eng': 'https://medium.com/@yasyf/come-hack-at-dorm-room-fund-4a38bbe8354c',
  '5years': 'https://5years.dormroomfund.com',
})

app = Flask(__name__)
app.config['DEBUG'] = bool(os.getenv('DEBUG'))
app.config['SERVER_NAME'] = SERVER_NAME

@app.route('/', subdomain="<subdomain>")
def redir(subdomain):
  return redirect(REDIRS[subdomain], code=301)
