from flask import Flask, render_template
from post import contents

app = Flask(__name__)


@app.route('/')
def home():
    all_posts = contents
    return render_template("index.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
