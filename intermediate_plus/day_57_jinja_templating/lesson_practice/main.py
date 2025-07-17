from flask import Flask, render_template
import random
import datetime
import requests
from content import contents

app = Flask(__name__)
current_year = datetime.datetime.now().year

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    guessed_gender = requests.get(f"https://api.genderize.io?name={name}").json().get("gender")
    guessed_age = requests.get(f"https://api.agify.io?name={name}").json().get("age")
    return render_template("guess.html", name=name, gender=guessed_gender, age=guessed_age, year=current_year)

@app.route('/blog/<num>')
def get_blog(num):
    # blog_url = "https://www.npoint.io/docs/43a04b9292442431b827"
    # response = requests.get(blog_url)
    print(num)
    all_posts = contents
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
