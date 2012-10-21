'''
Created on Oct 9, 2012

@author: jbelis
'''
import unittest
import time
import sys
import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import testbed

from mathdash import model

from optparse import OptionParser

def parse_command_line():
    parser = OptionParser()
    parser.add_option("-d", "--duration", dest="duration", help="game duration")
    parser.add_option("-a", "--answers", dest="count_answer", help="number of answers provided")
    parser.add_option("-t", "--correct", dest="count_answer_correct", help="number of correct answers provided")
    parser.add_option("-s", "--score", dest="score", help="score obtained", default=0)
    parser.add_option("-c", "--completed", dest="completed", help="true if game was completed", default=True)
    parser.add_option("-e", "--email", dest="email", help="test user email address")
    
    (options, args) = parser.parse_args()
    return options

def setCurrentUser(email, user_id, is_admin=False):
    os.environ['USER_EMAIL'] = email or ''
    os.environ['USER_ID'] = user_id or ''
    os.environ['USER_IS_ADMIN'] = '1' if is_admin else '0'

def logoutCurrentUser():
    setCurrentUser(None, None)

def main():
    options = parse_command_line()
    setCurrentUser(options.email, options.email)
    
    bed = testbed.Testbed()
    # Then activate the testbed, which prepares the service stubs for use.
    bed.activate()
    # Next, declare which service stubs you want to use.
    bed.init_datastore_v3_stub()
    bed.init_user_stub(True)
    bed.init_memcache_stub()

    user = users.get_current_user();
    print user
    
    # create a gamer
    gamer = model.Gamer(key_name = user.email(), creationtime=long(time.mktime(time.gmtime())))
    gamer.put()
    print gamer.key()
    
    ct = long(time.mktime(time.gmtime()))
    r = model.GameResult(creationtime=ct, 
                         game='belotte',
                         parent=gamer
                         )
    
    r.duration = int(options.duration)
    r.count_answer = int(options.count_answer)
    r.count_answer_correct = int(options.count_answer_correct)
    r.completed = bool(options.completed)
    r.score = int(options.score)
    r.put()
    
    print r
        
    # check that it is there
    gamer_k = db.Key.from_path('Gamer', options.email)
    print gamer_k;
    gamer = db.get(gamer_k)
    print gamer
    
    q = model.GameResult.all()
    q.ancestor(gamer)
    q.filter("creation_time = ", ct)
    rr = q.get()
    print rr.parent().email()
    
    
    bed.deactivate()
    logoutCurrentUser()


if __name__ == "__main__":
    main()
