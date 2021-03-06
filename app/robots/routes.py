from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from app.robots.bp import robot1
from app.robots.ibm.pcmiler.pcmiler_script import PCMiler
from werkzeug.utils import secure_filename

robots = Blueprint('robots', __name__)


@robots.route("/pcmiler", methods=['GET', 'POST'])
@login_required
def pcmiler():
    status = ""
    if request.method == 'POST':
        file = request.files['input_data']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        directory = f"{robots.root_path}\\ibm\\pcmiler\\"
        filename = secure_filename(file.filename)
        file.save(directory + filename)
        PCMiler(directory=directory, filename=filename)
        status = "Running program ..."
    elif request.method == 'GET':
        status = "Waiting for user input ..."
    return render_template('pcmiler.html', title="Olimpus: PC Miler", status=status)


@robots.route("/robot1")
@login_required
def robot():
    # robot1.status()
    return robot1.process()
