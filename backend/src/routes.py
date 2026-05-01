from flask import Blueprint, request, jsonify
from .database import db, User, Post, Comment, Like, ReadLater        # Note the dot (refers to database.py in same folder)
from . import bcrypt               # Refers to bcrypt initialized in __init__.py
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)

# ── Auth ──────────────────────────────────────────────────────────────────────

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Email and password are required"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Email already exists"}), 400

    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        first_name=data.get('first_name', ''),
        last_name=data.get('last_name', ''),
        email=data['email'],
        password_hash=hashed_pw,
        role=data.get('role', 'Reader')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Email and password are required"}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, data['password']):
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({
        "access_token": token,
        "user": {
            "id":         user.id,
            "first_name": user.first_name,
            "last_name":  user.last_name,
            "email":      user.email,
            "role":       user.role
        }
    }), 200


# ── Current user ──────────────────────────────────────────────────────────────

@api.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    user = User.query.get(int(get_jwt_identity()))
    if not user:
        return jsonify({"msg": "User not found"}), 404
    return jsonify({
        "id":         user.id,
        "first_name": user.first_name,
        "last_name":  user.last_name,
        "email":      user.email,
        "role":       user.role
    }), 200


@api.route('/me', methods=['PUT'])
@jwt_required()
def update_me():
    user = User.query.get(int(get_jwt_identity()))
    if not user:
        return jsonify({"msg": "User not found"}), 404

    data = request.get_json()
    user.first_name = data.get('first_name', user.first_name)
    user.last_name  = data.get('last_name',  user.last_name)
    db.session.commit()
    return jsonify({"msg": "Profile updated"}), 200


# ── Posts ─────────────────────────────────────────────────────────────────────

@api.route('/posts', methods=['GET'])
def get_posts():
    category = request.args.get('category')
    query = Post.query
    if category and category != 'All':
        query = query.filter_by(category=category)
    posts = query.order_by(Post.created_at.desc()).all()
    return jsonify([{
        "id":          p.id,
        "title":       p.title,
        "category":    p.category,
        "description": p.description,
        "content":     p.content,
        "user_id":     p.user_id,
        "created_at":  p.created_at.isoformat() if p.created_at else None,
        "author":      f"{p.author.first_name} {p.author.last_name}".strip() if p.author else "Anonymous"
    } for p in posts]), 200


@api.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    p = Post.query.get_or_404(post_id)
    return jsonify({
        "id":          p.id,
        "title":       p.title,
        "category":    p.category,
        "description": p.description,
        "content":     p.content,
        "user_id":     p.user_id,
        "created_at":  p.created_at.isoformat() if p.created_at else None,
        "author":      f"{p.author.first_name} {p.author.last_name}".strip() if p.author else "Anonymous"
    }), 200


@api.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({"msg": "Title and content are required"}), 400

    post = Post(
        title=data['title'],
        category=data.get('category', 'General'),
        description=data.get('description', ''),
        content=data['content'],
        user_id=int(get_jwt_identity())
    )
    db.session.add(post)
    db.session.commit()
    return jsonify({"msg": "Post created", "id": post.id}), 201


@api.route('/posts/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    user_id = int(get_jwt_identity())
    post = Post.query.get_or_404(post_id)
    if post.user_id != user_id:
        return jsonify({"msg": "Forbidden"}), 403

    data = request.get_json()
    post.title       = data.get('title',       post.title)
    post.category    = data.get('category',    post.category)
    post.description = data.get('description', post.description)
    post.content     = data.get('content',     post.content)
    db.session.commit()
    return jsonify({"msg": "Post updated"}), 200


@api.route('/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    user_id = int(get_jwt_identity())
    post = Post.query.get_or_404(post_id)
    if post.user_id != user_id:
        user = User.query.get(user_id)
        if not user or user.role not in ('Admin', 'Moderator'):
            return jsonify({"msg": "Forbidden"}), 403

    db.session.delete(post)
    db.session.commit()
    return jsonify({"msg": "Post deleted"}), 200


@api.route('/my-posts', methods=['GET'])
@jwt_required()
def my_posts():
    user_id = int(get_jwt_identity())
    posts = Post.query.filter_by(user_id=user_id).order_by(Post.created_at.desc()).all()
    return jsonify([{
        "id":         p.id,
        "title":      p.title,
        "category":   p.category,
        "created_at": p.created_at.isoformat() if p.created_at else None
    } for p in posts]), 200


# ── Admin ─────────────────────────────────────────────────────────────────────

def _get_admin_or_403():
    user = User.query.get(int(get_jwt_identity()))
    if not user or user.role != 'Admin':
        return None, (jsonify({"msg": "Admin access required"}), 403)
    return user, None


@api.route('/admin/users', methods=['GET'])
@jwt_required()
def admin_list_users():
    _, err = _get_admin_or_403()
    if err:
        return err
    users = User.query.all()
    return jsonify([{
        "id":         u.id,
        "first_name": u.first_name,
        "last_name":  u.last_name,
        "email":      u.email,
        "role":       u.role
    } for u in users]), 200


@api.route('/admin/posts/pending', methods=['GET'])
@jwt_required()
def admin_pending_posts():
    _, err = _get_admin_or_403()
    if err:
        return err
    posts = Post.query.order_by(Post.created_at.desc()).limit(20).all()
    return jsonify([{
        "id":       p.id,
        "title":    p.title,
        "category": p.category,
        "author":   f"{p.author.first_name} {p.author.last_name}".strip() if p.author else "Unknown"
    } for p in posts]), 200
