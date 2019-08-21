from models import Accounts
import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('/HTML/index.html')
        self.response.write(result_template.render())

class Loggedin(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("uName")
        password = self.request.get("pass")
        acc = Accounts(Username = username, Password = password)
        acc.put()
        var_dict = {
            "all_acc": Accounts.query().fetch(),
            "user": username,
            "pass": password
        }
        print(var_dict["all_acc"])
        result_template = the_jinja_env.get_template('/HTML/search.html')
        self.response.write(result_template.render(var_dict))

class Login(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('/HTML/login.html')
        self.response.write(result_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/loggedin', Loggedin),
    ('/login', Login)
], debug=True)
