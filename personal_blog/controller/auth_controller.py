from flask import Blueprint, render_template, request, redirect, url_for, flash,session
from flask_httpauth import HTTPBasicAuth
from flask import Blueprint
from personal_blog.models.forms import User
from functools import wraps

# onde auth_controlller busca os templates
auth_bp =  Blueprint("auth", __name__, template_folder="../views/templates")

# instacia o auth
auth = HTTPBasicAuth()

# user admin 
users = {
    "admin": {"password": "admin1234", "role": "admin"}
}



@auth.verify_password
def verify_password(username,password):
    # verifica  o usuario se existir
    user = users.get(username)

    if user and user['password'] == password:
        return username
    return None



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # rota pra login se o user for admin redireciona pra rota admin se nao pra rota login novamente da um feedback
    form = User()

    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = verify_password(username, password)

        if user:
            session['username'] = username
            session['role'] = users[username]['role']
            return redirect(url_for('post.admin'))
        
        else:
            flash("senha ou usuario errado")
            return render_template('login.html',form=form)
        
    return render_template('login.html',form=form)


# Decorador para verificar se o usuário é admin
def requires_admin(f):
    # se tentar acessa a rota protegida sem ta autenticado  redireciona para a página de login
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get("role") != "admin":
            flash("Você precisa ser administrador para acessar essa página.")
            return redirect(url_for('auth.login')) 
        
        return f(*args, **kwargs)
    
    return decorated
