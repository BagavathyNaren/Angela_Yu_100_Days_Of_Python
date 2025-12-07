from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv  
load_dotenv()  # take environment variables from .env.

# ✅ OMDb API setup
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
OMDB_API_URL = "http://www.omdbapi.com/"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///H:/100_Days_Of_Python_Coding_Angela_Yu/Day 64 - Advanced - My Top 10 Movies Website/instance/movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

    # # 🟢 Fetch "Phone Booth" from OMDb API
    # OMDB_API_KEY = os.getenv("OMDB_API_KEY")
    # response = requests.get("http://www.omdbapi.com/", params={
    #     "apikey": OMDB_API_KEY,
    #     "t": "Avatar: The Way of Water",
    #     "plot": "full"
    # })
    # data = response.json()

    # if data.get("Response") == "True":
    #     # ✅ Create Movie entry from API data
    #     new_movie = Movie(
    #         title=data["Title"], # type: ignore
    #         year=int(data["Year"]), # type: ignore
    #         description=data["Plot"], # type: ignore
    #         rating=float(data["imdbRating"]) if data["imdbRating"] != "N/A" else None, # type: ignore
    #         ranking=10, # type: ignore
    #         review="I heart the water.", # type: ignore
    #         img_url=data["Poster"] # type: ignore
    #     )

    #     db.session.add(new_movie)
    #     db.session.commit()
    #     print(f"✅ Added '{data['Title']}' ({data['Year']}) to database.")
    # else:
    #     print("❌ Movie not found or OMDb API error.")


        #  new_movie = Movie(
        #     title='Avatar: The Way of Water', # type: ignore
        #     year=2022, # type: ignore
        #     description="Jake Sully lives with his newfound family formed on the extrasolar moon Pandora. Once a familiar threat returns to finish what was previously started, Jake must work with Neytiri and the army of the Na'vi race to protect their home.", # type: ignore
        #     rating=7.5, # type: ignore
        #     ranking=10, # type: ignore
        #     review="I liked the water.", # type: ignore
        #     img_url="https://m.media-amazon.com/images/M/MV5BMWNlMWQyMTQtZjc5MC00NTljLTgxZTctZDZiZTBmODY5MTkyXkEyXkFqcGc@._V1_SX300.jpg" # type: ignore
        # )




class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(OMDB_API_URL, params={
            "apikey": OMDB_API_KEY,
            "s": movie_title
        })
        data = response.json()
        if data.get("Response") == "True":
            movie_list = data["Search"]
            return render_template("select.html", options=movie_list)
        else:
            return render_template("error.html", message="No movies found.")
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    imdb_id = request.args.get("id")
    if imdb_id:
        response = requests.get(OMDB_API_URL, params={
            "apikey": OMDB_API_KEY,
            "i": imdb_id,
            "plot": "full"
        })
        data = response.json()

        new_movie = Movie(
            title=data["Title"], # type: ignore
            year=int(data["Year"].split("–")[0]), # type: ignore
            img_url=data["Poster"], # type: ignore
            description=data["Plot"], # type: ignore
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))
    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        if form.rating.data is not None and form.rating.data != "":
            movie.rating = float(form.rating.data)
        else:
            movie.rating = None # type: ignore
        movie.review = form.review.data if form.review.data is not None else ""
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
