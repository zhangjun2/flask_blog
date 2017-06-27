#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import os

from flask import Flask, render_template, request, make_response, g, url_for, flash, session
from werkzeug.utils import redirect, secure_filename

from webapp import app
from webapp.database import db_session
from webapp.models import Blog, Blog_category, get_blog_category

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/<category_id>')
@app.route('/')
def home(category_id=None):
    username = request.cookies.get('username')
    id = request.cookies.get('userid')
    realname = request.cookies.get('realname')
    if username:
        if category_id is not None:
            articles = Blog.query.filter(Blog.category_id==category_id).order_by(Blog.id.desc()).all()
        else:
            articles = Blog.query.order_by(Blog.id.desc()).all()
        for ar in articles:
            ar.category_name = Blog_category.query.get(ar.category_id).category_name
        category = get_blog_category()
        return render_template('home.html', username=username,categorys=category, articles=articles)
    else:
        return redirect(url_for('user.login'))


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['fileName']
        f.save('/' + secure_filename(f.filename))

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()