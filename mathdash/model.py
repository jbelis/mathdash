'''
Created on Oct 8, 2012

@author: jbelis
'''
from google.appengine.ext import db


class Game(db.Model):
    creationtime = db.IntegerProperty(required=True)
    title = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    author = db.StringProperty()
    description = db.StringProperty()
    script = db.StringProperty()


class Gamer(db.Model):
    creationtime = db.IntegerProperty(required=True)
    
    def email(self):
        return self.key_name
    

class GameResult(db.Model):
    creationtime = db.IntegerProperty(required=True)
    game = db.StringProperty(required=True)
    duration = db.IntegerProperty()
    count_answer = db.IntegerProperty()
    count_answer_correct = db.IntegerProperty()
    score = db.IntegerProperty()
    completed = db.BooleanProperty()
    
