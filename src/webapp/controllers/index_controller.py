from flask import render_template
from src.core.web import app

@app.route('/')
def index():
    return render_template("index_view.html")