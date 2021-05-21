from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    redirect(url_for('static', filename='ds_ai_logo.png'), code=301)
    return "Welcome to Data Services & AI Website!"
