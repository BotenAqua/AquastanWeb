from flask import render_template
from project import app

@app.get('/')
def home():
	page_content = {'title': 'Wowowow', 'data': 'test'}
	return render_template('index.html', **page_content)
