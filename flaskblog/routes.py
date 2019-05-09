from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm


posts = [
    {
        'author': 'Corey',
        'title': 'Blog 1',
        'content': 'First Blog Content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Jane',
        'title': 'Blog 2',
        'content': 'Second Blog Content',
        'date_posted': 'April 22, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'yuemikhailzheng@gmail.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check in username and password!', 'danger')
    return render_template('login.html', title='Login', form=form)
