from flask import Blueprint, render_template

from app.robots.bp import robot1

robots = Blueprint('robots', __name__)


@robots.route("/pcmiler")
def pcmiler():
    return render_template('pcmiler.html', title="Olimpus: PC Miler")
    # TODO check methods


@robots.route("/robot1")
def robot():
    # robot1.status()
    return robot1.process()