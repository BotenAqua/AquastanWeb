from project import app

@app.route('/')
def home():
        return 'Hello, world! Again :-D'

