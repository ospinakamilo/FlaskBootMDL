from flask import render_template
from src.core.web import app

@app.route('/contact')
def contact():
    return render_template("contact_view.html")