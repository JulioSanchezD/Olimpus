from flask import Blueprint, render_template

robots = Blueprint('robots', __name__)


@robots.route("/pcmiler")
def pcmiler():
    return render_template('pcmiler.html', title="Olimpus: PC Miler")
