from flask import Flask, render_template
import requests 

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/b35ed8fac43ef21e0945")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post(id):
    response = requests.get(url="https://api.npoint.io/b35ed8fac43ef21e0945")
    all_posts = response.json()
    post = all_posts[id]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)