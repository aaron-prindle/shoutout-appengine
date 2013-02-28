#!/usr/bin/env python

import update_schema
import wsgiref.handlers
from google.appengine.ext import deferred
from google.appengine.ext import ndb
from google.appengine.ext import webapp
from google.appengine.ext.webapp \
     import template    

class Shout(ndb.Model):
    message = ndb.StringProperty(
        required=True)
    when = ndb.DateTimeProperty(
        auto_now_add=True)
    #ADDED
    author = ndb.StringProperty(
        required=True)


class MainHandler(webapp.RequestHandler):
    def get(self):
        shouts = ndb.gql(
        'SELECT * FROM Shout')
        values = {
            'shouts':shouts
        }
        self.response.out.write(
          template.render('main.html',values))
    def post(self):
        shout = Shout(
        message=self.request.get(
            'message'),author=self.request.get(
            'author') )
        shout.put()
        self.redirect('/')

class UpdateHandler(webapp.RequestHandler):
    def get(self):
        deferred.defer(update_schema.UpdateSchema)
        self.response.out.write('Schema migration successfully initiated.')

def main():
    app = webapp.WSGIApplication([
        (r'/',MainHandler),('/update_schema', UpdateHandler)], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
    main()
