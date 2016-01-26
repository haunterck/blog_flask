from app import app

@app.route('/')
def homepage():
    return 'HOME PAGE'
