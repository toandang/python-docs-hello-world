# from flask import Flask, render_template
# import os

# IMAGE_FOLDER = os.path.join('', 'images')

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# @app.route('/')
# @app.route('/index')
# def show_index():
#     full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'ds_ai_logo.png')
#     return render_template("index.html", user_image = full_filename)
from flask import Flask, flash, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome Data Services & AI World!"
	# return redirect(url_for('', filename='images/' + 'ds_ai_logo.png'), code=301)


# if __name__ == "__main__":
#     app.run()