from flask import Blueprint,render_template,request,redirect

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/<name>/')
def hello(name):
    return render_template('index.html',username=name)

@main.route('/login/')
def loginUser():
    return render_template('login.html') 

@main.route('/login/',methods = ['POST'])
def loginUserPost():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'admin':
        return redirect('/'+username)
    else:
        return 'Login Failed'

@main.route('/register/')
def registerUser():
    return render_template('register.html')