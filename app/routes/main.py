from flask import Blueprint,render_template,request,redirect,flash,url_for,session
import requests
from app import models

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if 'username' in session:
        return render_template('index.html',username = session['username'])
    else:
        return render_template('index.html')

@main.route('/login/',methods = ['GET','POST'])
def loginUser():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        api_url = 'http://localhost:5000/api/login'
        data = {'username': username, 'password': password}
        response = requests.post(api_url,data=data)
        if response.status_code == 200 and response.json().get('message') == 'Login successful':
            session['username'] = username
            session.pop('_flashes',None)
            return redirect(url_for('main.home'))
        else:
            flash('Login failed')
            return redirect(url_for('main.loginUser'))
    return render_template('login.html') 

@main.route('/register/',methods = ['GET','POST'])
def registerUser():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        api_url = 'http://localhost:5000/api/register'
        data = {'username': username, 'password': password}
        response = requests.post(api_url,data=data)
        if response.status_code == 200 and response.json().get('message') == 'Register successful':
            session['username'] = username
            session.pop('_flashes',None)
            return redirect(url_for('main.home'))
        else:
            flash('Register failed')
            return redirect(url_for('main.registerUser'))
    return render_template('register.html')

@main.route('/logout')
def logoutUser():
    session.pop('username', None)
    # flash('You have been logged out.')
    return redirect(url_for('main.home'))

@main.route('/get_users')
def get_users():
    users = models.User.query.all()  # 获取所有用户
    return '<br>'.join([f'{user.username} ({user.password})' for user in users])