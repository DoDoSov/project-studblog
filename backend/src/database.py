from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='Reader')
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.id),
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role
        }

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    banner_url = db.Column(db.String(500))
    description = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')
    # NEW: Popularity Tracking
    likes = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)

    # 3rd Party Data (GitHub)
    github_repo = db.Column(db.String(150), nullable=True)
    github_stars = db.Column(db.Integer, default=0)
    github_forks = db.Column(db.Integer, default=0)
    last_sync = db.Column(db.DateTime, nullable=True)

    author = db.relationship('User', backref=db.backref('posts', lazy=True))

    def to_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "category": self.category,
            "banner_url": self.banner_url,
            "description": self.description,
            "content": self.content,
            "user_id": str(self.user_id),
            "author_name": f"{self.author.first_name} {self.author.last_name}" if self.author else "Unknown",
            "created_at": self.created_at.isoformat(),
            "likes": self.likes,
            "views": self.views,
            "github_repo": self.github_repo,
            "github_stars": self.github_stars,
            "github_forks": self.github_forks,
            "last_sync": self.last_sync.isoformat() if self.last_sync else None
        }

# Logic tables for tracking interactions
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.BigInteger, db.ForeignKey('posts.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.id),
            "content": self.content,
            "user_id": str(self.user_id),
            "post_id": str(self.post_id),
            "created_at": self.created_at.isoformat()
        }

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.BigInteger, db.ForeignKey('posts.id'), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "post_id": str(self.post_id)
        }

class ReadLater(db.Model):
    __tablename__ = 'read_later'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.BigInteger, db.ForeignKey('posts.id'), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "post_id": str(self.post_id)
        }