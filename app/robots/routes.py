from flask import Blueprint, render_template, request, jsonify

robots = Blueprint('robots', __name__)


@robots.route("/pcmiler", methods=['GET', 'POST'])
def pcmiler():
    if request.method == 'POST':
        return jsonify({"result": request.get_array(field_name='input_data')})
    return render_template('pcmiler.html', title="Olimpus: PC Miler")
