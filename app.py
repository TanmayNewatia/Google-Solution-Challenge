from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['Secret Key'] = 'secrecy'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get('username', "")
    email = request.form.get('email', "")
    password = request.form.get('pw', "")
    conpw = request.form.get('conpw', "")
    existing_user_username = User.query.filter_by(
        username=username).first()
    existing_user_email = User.query.filter_by(
        id=email).first()
    if existing_user_username:
        raise ValidationError(
            'That username already exists. Please choose a different one.')
    if existing_user_email:
        raise ValidationError(
            'That user ID already exists. Please choose a different one.')
    if (password != conpw):
        return render_template('register.html', error="Passwords don't match")
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username', "")
    email = request.form.get('email', "")
    password = request.form.get('pw', "")
    user = User.query.filter_by(id=email).first()
    if user:
        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
