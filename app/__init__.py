from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'kdkddid][pobcabKKFc'
login_manager = LoginManager(app)
login_manager.login_view = "register"


from app import routes