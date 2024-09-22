from flask import Flask, render_template
from utils import contants

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("layout.html", title=contants.appName)