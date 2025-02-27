from flask import Blueprint,render_template,request,redirect,flash,url_for
import requests
from app import models


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/<name>/')
def hello(name):
    return render_template('index.html',username=name)

@main.route('/login/',methods = ['GET','POST'])
def loginUser():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        api_url = f'http://localhost:5000/api/login/{username}/{password}'
        response = requests.get(api_url)
        if response.status_code == 200 and response.json().get('message') == 'Login successful':
            flash('Login successful')
            return redirect(url_for('main.hello',name = username))
        else:
            flash('Login failed')
            return redirect(url_for('main.loginUser'))
    return render_template('login.html') 

@main.route('/register/',methods = ['GET','POST'])
def registerUser():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        api_url = f'http://localhost:5000/api/register/{username}/{password}'
        response = requests.get(api_url)
        if response.status_code == 200 and response.json().get('message') == 'Register successful':
            flash('Register successful')
            return redirect(url_for('main.hello',name = username))
        else:
            flash('Register failed')
            return redirect(url_for('main.registerUser'))
    return render_template('register.html')