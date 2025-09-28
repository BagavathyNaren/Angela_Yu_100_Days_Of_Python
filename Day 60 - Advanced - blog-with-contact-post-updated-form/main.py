from flask import Flask, render_template, request
import smtplib
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/451fde2f9c37eecbf1c9").json()
OWN_EMAIL = os.getenv("EMAIL")
OWN_PASSWORD = os.getenv("PASSWORD")

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    if not OWN_EMAIL or not OWN_PASSWORD:
        raise ValueError("Email or password environment variables are not set.")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route('/post/<blog_id>')
def post_blog(blog_id):
    post = posts[int(blog_id) - 1]
    title = post["title"]
    subtitle = post["subtitle"]
    author = post["author"]
    date = post["date"]
    content = post["body"]
    image = post["image"]
    return render_template("post.html", title=title, subtitle=subtitle, author=author,
                           date=date, content=content, image=image)


if __name__ == "__main__":
    app.run(debug=True)


# def get_blog():
# blogs = requests.get("https://api.npoint.io/451fde2f9c37eecbf1c9")
# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
#     all_blogs = blogs.json()
#     return all_blogs
