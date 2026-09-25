import os
from flask import Flask, redirect, send_from_directory

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


@app.route('/login.html')
@app.route('/login', methods=['POST'])
@app.route('/signup', methods=['POST'])
@app.route('/logout')
@app.route('/guest')
def auth_redirect():
    return redirect('/')


@app.route('/')
def home():
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory(BASE_DIR, filename)


if __name__ == '__main__':
    app.run(debug=True)