from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    # Mostrar o perfil do usuário pelo seu nome
    return f'User Name, {escape(username)}'


@app.route('/user/config/<uuid:id>')
def show_user_config(id):
    # Mostrara página de config do usuário pelo ID
    # Ex: 123e4567-e89n-12d3-a456-426614174000
    return f'User Identification: {id}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Mostrar a postagem com o id fornecido, id é um inteiro
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # Mostrar o subcaminho após /path/
    return f'Subpath {escape(subpath)}'
