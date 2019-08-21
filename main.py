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
        username = self.request.get("uName")
        password = self.request.get("pass")
    def post(self):
        acc = Accounts(Username = username, Password = password)
        acc.put()
        var_dict = {
            "all_acc": Accounts.query().fetch(),
            "user": username,
            "pass": password
        }
        print(var_dict["all_acc"])
        result_template = the_jinja_env.get_template('search.html')
        self.response.write(result_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
], debug = True)
