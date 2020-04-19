from core.web import app, render_view

@app.route('/')
def index():
    return render_view("index_view.html")