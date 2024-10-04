# app/controllers/post_controller.py

from flask import Blueprint,render_template
from personal_blog.models.post import Post


post_bp = Blueprint('post', __name__,template_folder='../views/templates')

@post_bp.route('/')
def home():
    posts = Post.get_all() # Exemplo de função que busca os posts
    
    return render_template('home.html',posts=posts)

@post_bp.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.get_by_id(post_id)  # Função que busca o post específico
    return render_template('post_content.html',post=post)
