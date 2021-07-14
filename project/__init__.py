from flask import Flask

app = Flask(__name__)

#from project import routes
from .landing_page.landing import landing
app.register_blueprint(landing, url_prefix="")
