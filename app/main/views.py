from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db

@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to Blogger'

    form = PostForm()

    if form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        post.save_post()
        return redirect(url_for('.index'))

    posts = Post.query.order_by(Post.timestamp.desc()).all()

    return render_template('index.html', form=form, posts=posts)