from google.appengine.ext import ndb

class Accounts(ndb.Model):
    Username = ndb.StringProperty(required = True)
    Password = ndb.StringProperty(required = True)
