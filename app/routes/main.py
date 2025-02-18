from flask import Blueprint,render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/login/')
def loginUser():
    return render_template('login.html') 

@main.route('/register/')
def registerUser():
    return render_template('register.html')