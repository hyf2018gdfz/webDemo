from flask import Blueprint,jsonify
from app import models,db

api = Blueprint('api', __name__)

@api.route('/login/<username>/<password>')
def apiLogin(username,password):
    user = models.User.query.filter_by(username=username).first()
    if user and user.password == password:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Login failed'}), 401
    
@api.route('/register/<username>/<password>')
def apiRegister(username,password):
    user = models.User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already exists'}), 400
    else:
        db.session.add(models.User(username=username,password=password))
        db.session.commit()
        return jsonify({'message': 'Register successful'}), 200