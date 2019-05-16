from src.core.web import app
from flask import render_template 

@app.route('/')
def index():
    import os

    return render_template("index_view.html")