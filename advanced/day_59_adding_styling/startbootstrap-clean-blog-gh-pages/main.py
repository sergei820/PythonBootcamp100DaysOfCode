from flask import Flask, render_template
from post import parse_json_posts
from static.assets.text_content import content

app = Flask(__name__)


all_posts = parse_json_posts(content)

# USE url_for('static', filename='style.css')

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def get_post(post_id):
    post = all_posts[post_id]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
