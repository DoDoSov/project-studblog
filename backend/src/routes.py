from flask import Blueprint, request, jsonify
from .database import db, User, Post, Comment, Like, ReadLater
import datetime, requests, re
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

api = Blueprint('api', __name__)

# ── GitHub Sync Helper ────────────────────────────────────────────────────────

def sync_github_data(post, repo_path=None):
    """
    Retrieves data from 3rd party server (GitHub) and saves to database.
    Fulfills the 'API connected to a database' requirement.

    Priority order for finding the repo path:
    1. Explicit repo_path argument (sent directly from the form field)
    2. [github: user/repo] tag embedded in post content (legacy fallback)
    """
    if not repo_path:
        match = re.search(r'\[github:\s*([\w.\-]+/[\w.\-]+)\]', post.content or '')
        repo_path = match.group(1).strip() if match else None

    if repo_path:
        post.github_repo = repo_path
        try:
            response = requests.get(
                f"https://api.github.com/repos/{repo_path}",
                headers={"Accept": "application/vnd.github+json"},
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                post.github_stars = data.get('stargazers_count', 0)
                post.github_forks = data.get('forks_count', 0)
                post.last_sync = datetime.datetime.utcnow()
            else:
                print(f"GitHub API returned {response.status_code} for {repo_path}")
        except Exception as e:
            print(f"GitHub Sync Error: {e}")
    else:
        post.github_repo = None
        post.github_stars = 0
        post.github_forks = 0
        post.last_sync = None

# ── Auth & Profile ────────────────────────────────────────────────────────────

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(data.get('password'), method='pbkdf2:sha256')
    new_user = User(
        email=data.get('email'),
        password_hash=hashed_password,
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        role='Reader'
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@api.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(email=data.get('email')).first()

        if not user or not check_password_hash(user.password_hash, data.get('password')):
            return jsonify({"error": "Invalid credentials"}), 401

        access_token = create_access_token(identity=str(user.id))
        return jsonify({
            "access_token": access_token,
            "user": user.to_dict()
        }), 200
    except Exception as e:
        return jsonify({"error": "Server error"}), 500

@api.route('/me', methods=['GET'])
@jwt_required()
def get_me():
    user_id = int(get_jwt_identity())
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

@api.route('/me', methods=['PUT'])
@jwt_required()
def update_me():
    user_id = int(get_jwt_identity())
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    # Update Name/Surname
    if 'first_name' in data:
        user.first_name = data.get('first_name')
    if 'last_name' in data:
        user.last_name = data.get('last_name')

    # Update Password (The missing part!)
    if 'new_password' in data and data.get('new_password').strip():
        # Hash the new password before storing it
        user.password_hash = generate_password_hash(data.get('new_password'), method='pbkdf2:sha256')

    try:
        db.session.commit()
        return jsonify({
            "msg": "Profile updated successfully",
            "user": user.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Could not update profile"}), 500

# ── Posts (Public & Author) ───────────────────────────────────────────────────

@api.route('/posts', methods=['GET'])
def get_posts():
    category = request.args.get('category')
    limit = request.args.get('limit', type=int) 
    
    query = Post.query.filter_by(status='Approved')
    
    if category and category != 'All':
        query = query.filter_by(category=category)
    
    query = query.order_by(Post.created_at.desc())
    if limit: query = query.limit(limit)
        
    posts = query.all()
    return jsonify([{
        "id": str(p.id), # Fixed: cast to string[cite: 3]
        "title": p.title,
        "category": p.category,
        "banner_url": p.banner_url, 
        "description": p.description,
        "content": p.content,
        "status": p.status,
        "created_at": p.created_at.isoformat() if p.created_at else None,
        "author": f"{p.author.first_name} {p.author.last_name}".strip() if p.author else "Anonymous"
    } for p in posts]), 200

@api.route('/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    try:
        numeric_id = int(post_id)
    except:
        return jsonify({"error": "Invalid ID"}), 400
        
    p = Post.query.get_or_404(numeric_id)
    return jsonify({
        "id": str(p.id), # Fixed: cast to string[cite: 3]
        "title": p.title,
        "category": p.category,
        "banner_url": p.banner_url, 
        "description": p.description,
        "content": p.content,
        "status": p.status,
        "created_at": p.created_at.isoformat() if p.created_at else None,
        "author": f"{p.author.first_name} {p.author.last_name}".strip() if p.author else "Anonymous"
    }), 200

@api.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    user_id = int(get_jwt_identity())
    
    post = Post(
        title=data['title'],
        category=data.get('category', 'Technology'), 
        description=data.get('description', ''),
        content=data['content'],
        banner_url=data.get('banner_url', ''),
        user_id=user_id,
        status='pending'
    )
    repo_field = data.get('github_repo', '').strip() or None
    sync_github_data(post, repo_path=repo_field)
    db.session.add(post)
    db.session.commit()
    return jsonify({"msg": "Post submitted for review", "id": str(post.id)}), 201

@api.route('/posts/<post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    user_id = int(get_jwt_identity())
    current_user = User.query.get(user_id)
    
    try:
        numeric_id = int(post_id)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid Post ID format"}), 400

    post = Post.query.get_or_404(numeric_id)
    
    if post.user_id != user_id and current_user.role != 'Admin':
        return jsonify({"msg": "Forbidden"}), 403

    data = request.get_json()
    
    if current_user.role == 'Admin' and 'status' in data:
        post.status = data.get('status')
    
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    
    repo_field = data.get('github_repo', '').strip() or None
    sync_github_data(post, repo_path=repo_field)
    db.session.commit()
    return jsonify({
        "msg": "Post updated successfully", 
        "status": post.status,
        "id": str(post.id) 
    }), 200

@api.route('/my-posts', methods=['GET'])
@jwt_required()
def my_posts():
    user_id = int(get_jwt_identity())
    posts = Post.query.filter_by(user_id=user_id).order_by(Post.created_at.desc()).all()
    return jsonify([{
        "id": str(p.id),
        "title": p.title,
        "category": p.category,
        "status": p.status,
        "created_at": p.created_at.isoformat() if p.created_at else None
    } for p in posts]), 200

# ── Admin Routes ──────────────────────────────────────────────────────────────

def _is_admin():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    return user and user.role == 'Admin'

@api.route('/admin/posts/pending', methods=['GET'])
@jwt_required()
def admin_pending_posts():
    if not _is_admin():
        return jsonify({"msg": "Admin access required"}), 403
    
    posts = Post.query.filter_by(status='pending').order_by(Post.created_at.desc()).all()
    return jsonify([{
        "id": str(p.id), # Precision safe[cite: 3]
        "title": p.title,
        "category": p.category,
        "content": p.description or p.content[:100],
        "author_name": f"{p.author.first_name} {p.author.last_name}" if p.author else "Unknown"
    } for p in posts]), 200

@api.route('/admin/posts/all', methods=['GET'])
@jwt_required()
def get_all_posts_admin():
    if not _is_admin():
        return jsonify({"msg": "Admin access required"}), 403
    
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([{
        "id": str(p.id), # Precision safe[cite: 3]
        "title": p.title,
        "status": p.status,
        "category": p.category,
        "author_name": f"{p.author.first_name} {p.author.last_name}" if p.author else "Unknown",
        "created_at": p.created_at.isoformat() if p.created_at else None
    } for p in posts]), 200

@api.route('/posts/<post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    
    try:
        numeric_id = int(post_id)
    except:
        return jsonify({"error": "Invalid ID"}), 400

    post = Post.query.get_or_404(numeric_id)
    
    if post.user_id != user_id and user.role not in ('Admin', 'Moderator'):
        return jsonify({"msg": "Forbidden"}), 403

    db.session.delete(post)
    db.session.commit()
    return jsonify({"msg": "Post deleted"}), 200

# ── Static & Branding ─────────────────────────────────────────────────────────

@api.route('/about-static', methods=['GET'])
def get_about_static():
    return jsonify({
        "mission": "To bridge the gap between academic theory and real-world application through student-led storytelling.",
        "active_writers": "1,240+",
        "steps": [
            {"id": "STEP 01", "title": "Create an Account", "desc": "Sign up with your university email.", "icon": "✍️"},
            {"id": "STEP 02", "title": "Write Your Post", "desc": "Use the rich text editor.", "icon": "📝"},
            {"id": "STEP 03", "title": "Editor Reviews", "desc": "Ensuring quality guidelines.", "icon": "✅"},
            {"id": "STEP 04", "title": "Go Live & Share", "icon": "🌍", "desc": "Published on the platform."}
        ]
    }), 200

@api.route('/branding', methods=['GET'])
def get_branding():
    return jsonify({
        "site_name": "Student Blog",
        "slogan": "Share Knowledge, Empower Peers",
        "logo_url": "/assets/logo.png",
        "version": "1.0.0"
    }), 200