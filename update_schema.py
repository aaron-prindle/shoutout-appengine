import main
from google.appengine.ext import ndb


#for more: https://developers.google.com/appengine/articles/update_schema
def UpdateSchema(cursor=None, num_updated=0):
    query = ndb.gql(
        'SELECT * FROM Shout')
    
    for p in query:
        if p.author == "Anonymous" or p.author == None:
            p.author = "New Name"
            p.put()
