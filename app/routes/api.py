from flask import Blueprint,jsonify,request
from app import models,db

api = Blueprint('api', __name__)

@api.route('/login/',methods = ['POST'])
def apiLogin():
    username = request.form.get('username')
    password = request.form.get('password')
    user = models.User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401
    
@api.route('/register/',methods = ['POST'])
def apiRegister(username,password):
    username = request.form.get('username')
    password = request.form.get('password')
    user = models.User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already exists'}), 400
    else:
        user = models.User(username=username,password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Register successful'}), 200