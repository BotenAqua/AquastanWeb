from flask import Flask

app = Flask(__name__)

from project.landing_page import landing
app.register_blueprint(landing, url_prefix="")

from project.posts import posts
app.register_blueprint(posts, url_prefix="/p")
