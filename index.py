from flask import render_template
from flask.views import MethodView

class Index(MethodView):
   def get(self):
    # this page will go to the index html page which shows (main page), which shows what 
    #are the options available on the main page when the url is clicked
    return render_template("index.html")