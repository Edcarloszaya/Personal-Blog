# manage.py

from flask import Flask
from personal_blog.controller.post_controller import post_bp

# Configurando o caminho customizado para a pasta de templates
app = Flask(__name__)

# Registra as rotas
app.register_blueprint(post_bp)


if __name__ == '__main__':
    app.run(debug=True)
