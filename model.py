from app import db

class lyricModel(db.Model):
    __tablename__ = 'lyrics'
    __table_args__ = {'extend_existing': True}

    index = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String)
    poemName = db.Column(db.String)
    text = db.Column(db.String)
    syllables = db.Column(db.String)
    usage = db.Column(db.Integer)