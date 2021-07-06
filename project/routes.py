from flask import render_template
from project import app

@app.get('/')
def home():
        return render_template('index.html', title='Wowowowo', data='test')

