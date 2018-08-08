# -*- coding: utf-8 -*-
import webapp2
import jinja2
import os
from artist_service import artist_info

artist_ids={
    "Kendrick Lamar": "2YZyLoL8N0Wb9xBt1NhZWg",
    "Juice WRLD": "4MCBfE4596Uoi2O4DtmEMz",
    "Childish Gambino": "73sIBHcqh3Z3NyqHKZ7FOL",
    "Cardi B": "4kYSro6naA4h99UJvo89HB",
    "Abba" : "0LcJLqbBmaGUft1e9Mm8HV",
}

jinja_current_directory = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template("templates/welcome.html")
        self.response.write(welcome_template.render())

class ArtistsHandler(webapp2.RequestHandler):
    def get(self):
        artists_template = jinja_current_directory.get_template("templates/artists.html")
        self.response.write(artists_template.render())

class ArtistHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get("name")
        artist_template = jinja_current_directory.get_template("templates/artist.html")
        self.response.write(artist_template.render({"name": name, "artist_id": artist_info[name]["artist_id"], "image": artist_info[name]["image"]}))

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/artists', ArtistsHandler),
    ('/artist', ArtistHandler),
], debug=True)
