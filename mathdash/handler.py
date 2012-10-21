'''
Created on Oct 8, 2012

@author: jbelis
'''

import os
import logging
import time
import json

import webapp2

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from webapp2_extras import i18n

from google.appengine.ext import db

from mathdash import model
from mathdash import strings

def get_current_gamer():
    user = users.get_current_user();
    if user:
        gamer_k = db.Key.from_path('Gamer', user.email())
        gamer = db.get(gamer_k)
        if gamer == None:
            gamer = model.Gamer(key_name=user.email(), creationtime=long(time.mktime(time.gmtime())))
            gamer.put()
        return gamer
    else:
        return None


class BaseHandler(webapp2.RequestHandler):
    def init_model(self):
        # Set the requested locale.        
        locale = self.request.GET.get('locale', 'en_US')
        if locale:
            i18n.get_i18n().set_locale(locale)
        logging.info(i18n.get_i18n().locale)
        
        user = users.get_current_user()

        modl = dict()
        strings.add_to_model(modl)
                    
        if user:
            modl['user'] = {
                'email': user.email(),
                'nickname': user.nickname(),
                'id': user.user_id()
            }
            modl['email'] = user.email()
            modl['login_url'] = '#'
            modl['logout_url'] = users.create_logout_url(self.request.uri)

        else :
            modl['user'] = 'null'
            modl['email'] = ''
            modl['login_url'] = users.create_login_url(self.request.uri)
            modl['logout_url'] = '#'

        return modl;
    


class ResultHandler(BaseHandler):

    def post(self):
        gamer = get_current_gamer();
        if gamer:
            r = model.GameResult(creationtime = long(time.mktime(time.gmtime())),
                                 game=self.request.params['game'],
                                 parent=gamer)
            r.duration = int(self.request.params['duration'])
            r.completed = bool(self.request.params['completed'])
            r.score = int(self.request.params['score'])
            r.count_answer_correct = int(self.request.params['count_answer_correct'])
            r.count_answer = int(self.request.params['count_answer'])
            r.put()
        else:
            handle_401(self);
            
    
    def get(self):
        gamer = get_current_gamer();
        if gamer:
            k = None
            if self.request.GET.get('creationtime'):
                k = db.Key.from_path('Gamer', gamer, 'GameResult', self.request.get('key'))
                
            if k:
                r = db.get(k)
                if r:
                    json.dump(r, self.response)
                else:
                    handle_404(self, "invalid key: " + k)
            else:
                handle_404(self, "no game result matching creation time " + self.request.get('creationtime'))
        else:
            handle_401(self);
        

    def delete(self):
        gamer = get_current_gamer();
        if gamer:
            k = db.Key.from_path('User', gamer, 'GameResult', self.request.get('key'))
            if k:
                db.delete(k)
        else:
            handle_401(self);



class ResultHistoryHandler(BaseHandler):
        
    def get(self):
        modl = self.init_model()
        gamer = get_current_gamer()
        if gamer:
            q = model.GameResult.all()
            q.ancestor(gamer)
            q.order('-creationtime')
            limit = self.request.GET.get('limit')
            
            l = list()
            d = dict()
            for p in q.run():
                if (not d.has_key(p.game)):
                    d[p.game] = {
                        'name': p.game,
                        'data': list()
                    }
                    
                l = d[p.game]['data']
                l.append([p.creationtime * 1000, p.score])

            s = json.dumps(d.values())
            
            modl['history'] = s
            
            path = os.path.join(os.path.dirname(__file__), '../templates/history.html')
            self.response.out.write(template.render(path, modl))
       

        else:
            handle_401(self);


def handle_error(handler, message, status):
    err = {
        'reason': message
    }
    json.dump(err, handler.response)
    handler.response.set_status(status)

def handle_401(handler):
    handle_error(handler, 'this request requires authentication', 401)
        
def handle_404(handler, message):
    handle_error(handler, message, 404)
    



