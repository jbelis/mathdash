#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import json

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from mathdash import handler, model

class MainHandler(handler.BaseHandler):
    def get(self):
        modl = self.init_model()
        
        # get the games
        script = []
        games = dict()
        q = model.Game.all()
        for game in q.run():
            script.append(game.script)
            script.append('\n')
            games[game.name] = {
                'title': game.title,
                'description': game.description
            }
            
        modl['games'] = json.dumps(games)
        modl['gamecode'] = ''.join(script)
        
        logging.info(modl)
        
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, modl))


routes = [
    ('/', MainHandler),
    ('/result', handler.ResultHandler),
    ('/history', handler.ResultHistoryHandler)
]

config = {}
config['webapp2_extras.i18n'] = {
    'translations_path': 'locale',
}

app = webapp2.WSGIApplication(routes=routes, debug=True, config=config)
