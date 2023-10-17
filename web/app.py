from flask import Flask
from config import Config
from auth.views import auth_blueprint
from auth import db,bctrypt,login_manager

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth_blueprint)

db.init_app(app)
bctrypt.init_app(app)
login_manager.init_app(app)


# init create db
with app.app_context(): 
    db.create_all()


if __name__ == "__main__":
    
    app.run()