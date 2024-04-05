from flask import Flask, render_template

app = Flask(__name__, template_folder='views', static_folder='views/assets')

@app.route('/')
def index():
    return render_template('index.html', name='Yoda', movies=[])