'''
Created on Oct 9, 2012

@author: jbelis
'''
import unittest
import datetime
import time

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import testbed

from mathdash import model

class Test(unittest.TestCase):


    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub(True)
        #self.testbed.init_memcache_stub()


    def tearDown(self):
        self.testbed.deactivate()


    def testPut(self):
        user = users.get_current_user();
        r = model.GameResult(email = user.email(), creationtime=time.mktime(datetime.datetime.now()),
                             parent=user)
        r.duration = self.request.get('duration')
        r.count_answer = self.request.get('count_answer')
        r.count_answer_correct = self.request.get('count_correct_answer')
        r.completed = self.request.get('completed')
        r.score = self.request.get('score')
        r.put()
        
        # check that it is there
        self.assertEqual(1, len(model.GameResult.all().fetch(2)))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()