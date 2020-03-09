from flask import Blueprint, render_template, request, jsonify

from app.robots.bp import robot1

robots = Blueprint('robots', __name__)


@robots.route("/pcmiler", methods=['GET', 'POST'])
def pcmiler():
    if request.method == 'POST':
        return jsonify({"result": request.get_array(field_name='input_data')})
    return render_template('pcmiler.html', title="Olimpus: PC Miler")
    # TODO check methods


@robots.route("/robot1")
def robot():
    # robot1.status()
    return robot1.process()
