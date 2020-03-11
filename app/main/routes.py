from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user, logout_user
from app import bcrypt, login_manager
from app.models import User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """Default page, if the user has alredy logged in he will be redirected to the home page,
        otherwise he is going to be redirected to the login page."""
    if current_user.is_authenticated:
        return render_template('home.html', title="Olimpus")
    else:
        return redirect(url_for('main.login'))


@login_manager.user_loader
def load_user(user_id):
    """Function that returns the user_id number of a particular user"""
    return User.query.get(int(user_id))


@main.route("/login", methods=['GET', 'POST'])
def login():
    """Login function that is only called by the login page whenever a user tries to login,
    this function gets the submit information and verifies that the data matches with the db data.
    If the information is validated, then the function redirects the user to the home page and creates
    a login object for the user."""
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user, False)
            return redirect(url_for('main.home'))
        else:
            flash("Wrong credentials", "danger")
    return render_template('login.html', error=error)


@main.route("/logout")
def logout():
    """This function logs out the user using the login object, so the user will be automatically redirected to the
    login page """
    logout_user()
    return redirect(url_for('main.login'))
