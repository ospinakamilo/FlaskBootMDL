from src.core.web import app, render_view

@app.route('/brython')
def contact():
    return render_view("brython_view.html")