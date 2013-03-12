import time
import main
from google.appengine.ext import deferred
from google.appengine.ext import ndb

BATCH_SIZE = 1  # ideal batch size may vary based on entity size.

#for more: https://developers.google.com/appengine/articles/update_schema
def UpdateSchema(cur_offset=0):
    query = main.Shout.query()

    to_put=[]
    for p in query.fetch(limit=BATCH_SIZE, offset=cur_offset):
        p.author = "IT WORKS!!!!" #altering prexisting field/adding a default value to a newly created field (as app engine will add field to new things when added to model)
        #delattr(p, 'author') #http://sandrylogan.wordpress.com/2010/12/08/delattr/  'need to add db.Expando to the model also'
        to_put.append(p)

            
    if to_put:
        p.put()
        time.sleep(60)
        deferred.defer(
            UpdateSchema, cur_offset= cur_offset + BATCH_SIZE)