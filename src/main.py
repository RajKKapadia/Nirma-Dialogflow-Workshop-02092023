from flask import Flask

app = Flask(__name__)

@app.route('/')
def handle_home():
    return 'OK', 200
