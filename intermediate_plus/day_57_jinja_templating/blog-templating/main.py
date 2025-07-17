from flask import Flask, render_template
from static.content import contents
from post import parse_json_posts

app = Flask(__name__)

all_posts = parse_json_posts(contents)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    post = all_posts[post_id]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
