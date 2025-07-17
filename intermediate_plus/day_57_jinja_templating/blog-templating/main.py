from flask import Flask, render_template
from static.content import contents as all_posts

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<post_id>')
def get_post(post_id):
    post = all_posts[int(post_id) - 1]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
