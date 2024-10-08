from datetime import datetime
from itsdangerous import TimestampSigner
from hello import db, login_manager
from flask import current_app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self):
        s = TimestampSigner(current_app.config['SECRET_KEY'])
        return s.sign("{'user_id': 1}")
     
    @staticmethod
    def verify_reset_token(token, expired_sec=1800):
        s = TimestampSigner(current_app.config['SECRET_KEY'])
        try:
            user_id = s.unsign(token, max_age=expired_sec)['user_id']
        except:
            return None
        return User.query.get_or_404(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', {self.date_posted}')"