from flask import Flask, render_template
import os

IMAGE_FOLDER = os.path.join('static', '')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'ds_ai_logo.png')
    return render_template("index.html", user_image = full_filename)