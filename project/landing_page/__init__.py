from flask import Blueprint, render_template

landing = Blueprint("landing", __name__, template_folder="templates")

@landing.route("/")
def landing_page():
	page_content = {'title': 'Wowowow', 'data': 'landing page template'}
	return render_template('landing_page.html', **page_content)

@landing.route("/test")
def global_test():
        page_content = {'title': 'Test', 'data': 'global template'}
        return render_template('index.html', **page_content)
