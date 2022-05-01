from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    maintext = db.Column(db.Text(), nullable=False)
    type_of_press = db.Column(db.String(20), nullable=False)
    type_of_event = db.Column(db.String(20), nullable=False)
    likes = db.Column(db.Integer, primary_key=False)
    dislikes = db.Column(db.Integer, primary_key=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id', ondelete='CASCADE'))
    article = db.relationship('Article', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)