
from flask import Blueprint, render_template, request, redirect, url_for, flash
from personal_blog.models.post import Post
from personal_blog.models.forms import EditPost, NewPost
from personal_blog.controller.auth_controller import requires_admin

# onde a  post_controller busca os templates
post_bp = Blueprint("post", __name__, template_folder="../views/templates")


@post_bp.route("/")
def home():
    # home lista todos os posts
    posts = Post.get_all()

    return render_template("home.html", posts=posts)


@post_bp.route("/post/<int:post_id>")
def post_detail(post_id):
    # mostra um post especifico pelo id
    post = Post.get_by_id(post_id)

    return render_template("post_content.html", post=post)


@post_bp.route("/admin")
@requires_admin
def admin():
    # requer admin logado pra acessa os post e pra delete edit e add novos post
    posts = Post.get_all()

    return render_template("admin.html", posts=posts)


@post_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
@requires_admin
def edit(post_id):
    # editar um post especifico pelo id e exibir um feedback
    post = Post.get_by_id(post_id)

    form = EditPost()

    if request.method == "POST" and form.validate_on_submit():
        post["title"] = form.title.data
        post["date"] = form.published_date.data
        post["content"] = form.content.data

        Post.edit_post(post, post_id)

        flash("post atualizado com sucesso")
        return redirect(url_for("post.admin"))

    return render_template("edit.html", form=form, post=post)


@post_bp.route("/new", methods=["GET", "POST"])
@requires_admin
def new_post():
    # adiciona um novo post e exibir um feedback
    post = {}

    form = NewPost()

    if request.method == "POST" and form.validate_on_submit():
        post["title"] = form.title.data
        post["date"] = form.published_date.data
        post["content"] = form.content.data
        Post.create(post)

        flash("post criado com sucesso")
        return redirect(url_for("post.admin"))

    return render_template("new.html", form=form)


@post_bp.route("/delete/<int:post_id>", methods=["GET"])
@requires_admin
def delete(post_id):
    # deletar um post e exibir um feedback
    Post.delete(post_id)
    flash("post deletado com sucesso")

    return redirect(url_for("post.admin"))
