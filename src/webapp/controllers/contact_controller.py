from src.core.web import app, render_view

@app.route('/contact')
def contact():
    return render_view("contact_view.html")