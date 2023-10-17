
from flask_login import UserMixin
from . import db,bctrypt,login_manager



@login_manager.user_loader
def user_loader(id):
    user = User.query.get(int(id))
    return user


class User(db.Model,UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    