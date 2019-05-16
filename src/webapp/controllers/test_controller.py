from src.core.web import app 

@app.route('/test')
def test():
    return "This is a test"