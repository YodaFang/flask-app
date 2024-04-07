from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()
from db.base import Base

app = Flask(__name__, template_folder='views', static_folder='views/assets')

@app.before_first_request
def before_first_request():
    Base.init_db()

@app.route('/')
def index():
    return render_template('index.html', name='Yoda', movies=[])