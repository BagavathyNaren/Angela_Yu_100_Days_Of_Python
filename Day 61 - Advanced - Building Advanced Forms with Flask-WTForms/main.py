from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label='Email', validators=[DataRequired(), Email(message='Please enter a valid email address.'), Length(min=5)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In", render_kw={"class": "btn btn-primary btn-lg"})


app = Flask(__name__)
app.secret_key = "mysecretkey"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

     # Debug: Print form validation results
    if request.method == 'POST':
        print("Form submitted")
        print("Valid:", login_form.validate())
        print("Errors:", login_form.errors)
        print("Email data:", login_form.email.data)

    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
             print("Form validated successfully!")
             return render_template("success.html")
        else:
            print("Form validation failed!")
            print("Errors:", login_form.errors)
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)