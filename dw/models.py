from dw import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)   
    message = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return '<Contact %r>' % self.id

class User(db.Model,UserMixin):
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(60), nullable=False)
    
#adated from Grinberg(2014, 2018)
    @property
    def password(self):
        raise AttributeError('Password is not readable.')

    @password.setter
    def password(self,password):
        self.hashed_password=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Pforms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), db.ForeignKey('user.id'), unique=True, nullable=False)
    message= db.Column(db.Text, nullable=False)
    
    def repr(self):
        return '<Pforms %r>' % self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))







    
    
