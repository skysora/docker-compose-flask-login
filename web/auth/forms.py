from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from .models import User


class RegisterForm(FlaskForm):
    
    username = StringField('Username',validators = [DataRequired(),Length(min=3,max=20)])
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=20)])
    confirm = PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already taken,please chosse anthor username")
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already taken,please chosse anthor username")
        
        
class LoginForm(FlaskForm):
    
    username = StringField('Username',validators = [DataRequired(),Length(min=3,max=20)])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=20)])
    remember  = BooleanField('Remember', default=True)