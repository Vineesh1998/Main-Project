from enum import unique
from wnd import db,app,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    return Login.query.get(int(id))



class Login(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    age = db.Column(db.String(80))
    weight = db.Column(db.String(80))
    height = db.Column(db.String(80))
    password = db.Column(db.String(80), nullable=False)
    usertype = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(200))
    contact = db.Column(db.String(200))



class Wound(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(80))
    val = db.Column(db.String(80))
    dat = db.Column(db.String(80))
    st = db.Column(db.String(80))











    
  
