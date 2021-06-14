from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/data.db'
db = SQLAlchemy(app)

class lyricModel(db.Model):
    __tablename__ = 'data'
    __table_args__ = {'extend_existing': True}

    index = db.Column(db.Integer, primary_key=True)
    singer = db.Column(db.String)
    song = db.Column(db.String)
    lyrics = db.Column(db.String)
    syllables = db.Column(db.String)
    usage = db.Column(db.Integer)
