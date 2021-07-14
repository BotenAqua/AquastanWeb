from flask import Blueprint, render_template

landing = Blueprint("landing", __name__)

@landing.route("/")
def landing_page():
	page_content = {'title': 'Wowowow', 'data': 'test'}
	return render_template('index.html', **page_content)

