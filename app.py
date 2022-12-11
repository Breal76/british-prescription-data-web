from flask import Flask

app = Flask(__name__) # references this filename

# Create index route so we don't 404 (in Flask we use app.route decorator)
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True) 