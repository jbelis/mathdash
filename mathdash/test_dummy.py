'''
Created on Oct 9, 2012

@author: jbelis
'''
import unittest

import webtest


class ResultTest(unittest.TestCase):

    def setUp(self):
        # Create a WSGI application.
        # self.testapp = webtest.TestApp(app)
        pass

    def tearDown(self):
        pass 

    def testPost(self):
        print 'in testPost'


#suite = unittest.TestLoader().loadTestsFromTestCase(ResultTest)
#unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unittest.main()
