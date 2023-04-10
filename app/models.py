# Add any model classes for Flask-SQLAlchemy here
from . import db
from sqlalchemy.sql import func

class Movies(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique = True)
    description = db.Column(db.Text, unique = True)
    poster = db.Column(db.String(50), unique = True)
    created_at = db.Column(db.DateTime)

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

    def __repr__(self):
        return '<Movies %r>' % self.title