import pdb
from unicodedata import name
from flask import Flask, flash, render_template, request, url_for, redirect


app = Flask(__name__, template_folder='template')

@app.route('/')
def index():   
    return render_template('index.html')

@app.route('/home')
def home():   
    return render_template('index.html')

@app.route('/about')
def about():   
    return render_template('about.html')

@app.route('/service')    
def service():
    return render_template('service.html')
if __name__ == '__main__':
    app.run(debug=True, port=8002)