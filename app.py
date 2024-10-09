# manage.py

from flask import Flask
from personal_blog.controller.post_controller import post_bp
from personal_blog.controller.auth_controller import auth_bp


app = Flask(__name__)

# configura secret_key 
app.config['SECRET_KEY'] = 'asugsuifghsaipghaispghipasghipasghipasghpa'

# Registra as rotas
app.register_blueprint(post_bp)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(debug=True)
