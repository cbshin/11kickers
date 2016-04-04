import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         logging.info(self.request.path)
#     	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
#     	self.response.write(template.render())

# class KickerHandler(webapp2.RequestHandler):
#     def get(self):
#         logging.info(self.request.path)
#     	template = JINJA_ENVIRONMENT.get_template('templates/profile.html')
#     	self.response.write(template.render(
#             ))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
            template = JINJA_ENVIRONMENT.get_template('templates/kickers%s' % self.request.path)
            if (self.request.path == '/stephen-gostkowski.html'):
                variables = {
                    'title': 'Stephen Gostkowski',
                    'quote': 'I\'m definitely more valuable than Tom Brady.'
                }
            elif (self.request.path == '/adam-vinatieri.html'):
                variables = {
                    'title': 'Adam Vinatieri',
                    'quote': 'Some say I use Touch of Grey. I do.'
                }
            elif (self.request.path == '/steven-hauschka.html'):
                variables = {
                    'title': 'Steven Hauschka',
                    'quote': 'What\'s a seahawk?'
                }
            elif (self.request.path == '/justin-tucker.html'):
                variables = {
                    'title': 'Justin Tucker',
                    'quote': 'Yeah of course I\'m terrified of Ray Lewis.'
                }
            elif (self.request.path == '/matt-prater.html'):
                variables = {
                    'title': 'Matt Prater',
                    'quote': 'Do you want to switch teams?'
                }
            elif (self.request.path == '/brandon-mcmanus.html'):
                variables = {
                    'title': 'Brandon McManus',
                    'quote': 'Peyton\'s forehead is larger in real person.'
                }
            elif (self.request.path == '/mason-crosby.html'):
                variables = {
                    'title': 'Mason Crosby',
                    'quote': 'Yeah the whole team get\'s discount double checks.'
                }
            elif (self.request.path == '/chandler-catanzaro.html'):
                variables = {
                    'title': 'Chandler Catanzaro',
                    'quote': 'Who do you know here?'
                }
            elif (self.request.path == '/robbie-gould.html'):
                variables = {
                    'title': 'Robbie Gould',
                    'quote': 'I don\'t have a foot of \'gould\', it\'s just flesh and bone.'
                }
            elif (self.request.path == '/graham-gano.html'):
                variables = {
                    'title': 'Graham Gano',
                    'quote': 'The Dab was my idea first.'
                }
            elif (self.request.path == '/cody-parkey.html'):
                variables = {
                    'title': 'Cody Parkey',
                    'quote': 'I\'m only on here because they needed an 11th kicker.'
                }
            elif (self.request.path == '/rankings.html'):
                variables = {
                    'title': 'Rankings',
                    'quote': 'The best kickers can open multiple jars of pickles.'
                }
            self.response.write(template.render(variables))
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/stephen-gostkowski.html', MainHandler),
    ('/adam-vinatieri.html', MainHandler),
    ('/steven-hauschka.html', MainHandler),
    ('/justin-tucker.html', MainHandler),
    ('/matt-prater.html', MainHandler),
    ('/brandon-mcmanus.html', MainHandler),
    ('/mason-crosby.html', MainHandler),
    ('/chandler-catanzaro.html', MainHandler),
    ('/robbie-gould.html', MainHandler),
    ('/graham-gano.html', MainHandler),
    ('/cody-parkey.html', MainHandler),
    ('/rankings.html', MainHandler),
], debug=True)