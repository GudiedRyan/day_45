from flask import Flask, render_template, request
import requests 
import os
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/b35ed8fac43ef21e0945")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", head = "Contact Me")
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user='yesmanvong@gmail.com', password=os.environ['yesmanvongpass'])
            connection.sendmail(
                from_addr=email,
                to_addrs="yesmanvong@gmail.com",
                msg=f"Subject: {name} would like to get in touch \n\n{message}\nPlease get back to me at either {email} or {phone}."
            )

        return render_template("contact.html", head = "Successfully sent your message!")

@app.route('/post/<int:id>')
def post(id):
    response = requests.get(url="https://api.npoint.io/b35ed8fac43ef21e0945")
    all_posts = response.json()
    post = all_posts[id]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)