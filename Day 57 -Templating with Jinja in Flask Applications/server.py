from flask import Flask, render_template
import random
from datetime import datetime as time
import requests

app = Flask(__name__)

print(f"Name of the app: {__name__}")

name_of_person = "Naren Bagavathy"

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = time.now().year
    return render_template('index.html', num=random_number, year=current_year, name=name_of_person)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(url=gender_url)
    gender_data = gender_response.json()
    person_gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(url=age_url)
    age_data = age_response.json()
    person_age = age_data["age"]
    return render_template('guess.html', person_name=name, age=person_age, gender=person_gender )

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/e9a5e16430a229ca3520"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


