from flask import Blueprint, render_template

posts = Blueprint("posts", __name__, template_folder="templates", static_folder="static")

@posts.route("/")
def global_test():
        page_content = {'title': 'Posts', 'data': 'posts blueprint <3'}
        return render_template('test.html', **page_content)
