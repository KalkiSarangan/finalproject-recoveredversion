from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'finalprojectkey'
app.config['UPLOAD_FOLDER'] = 'files'
#model = load_model('model.h5')

class statistics():
    home = 0
    upload = 0
    admin = 0
    prediction = 0
    xray = 0

stats = statistics()

class Upload(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    stats.home = stats.home + 1
    return "Osteoarthritis detection from xray"

@app.route('/xray', methods=['GET', 'POST'])
def xray_login():
    stats.xray = stats.xray + 1
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'technician' and request.form['password'] == 'xray':
            return redirect(url_for('upload'))
        else:
            error = "You're not authorized to use this."
    return render_template('login.html', error=error)

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    stats.admin = stats.admin + 1
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'secret':
            return render_template('statistics.html', home=stats.home, xray=stats.xray,upload=stats.upload, prediction=stats.prediction, admin=stats.admin)
    else:
        error = "You're not authorized to access this."
    return render_template('login.html', error=error)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    stats.upload = stats.upload + 1
    form = Upload()
    if form.validate_on_submit():
        file = request.files['file']
        file_path = 'files/' + file.filename
        file.save(file_path)
        return redirect(url_for('prediction', file_path=file_path))
    return render_template('index.html', form = form)

@app.route('/predict', methods=['GET', 'POST'])
def prediction(file_path):
   # stats.prediction = stats.prediction + 1
   #  i = image.load_img(file_path, target_size=(256, 256))
   # p = model.predict(i)
    return "WIP"  # decode_predictions(p)[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
