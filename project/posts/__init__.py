from flask import Blueprint, render_template

posts = Blueprint("posts", __name__, template_folder="templates")

@posts.route("/")
def global_test():
        page_content = {'title': 'Posts', 'data': 'posts blueprint <3'}
        return render_template('index.html', **page_content)
