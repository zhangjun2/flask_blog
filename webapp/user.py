from flask import Blueprint, render_template, request, session, flash, make_response, url_for
from sqlalchemy import func
from werkzeug.utils import redirect

from webapp.database import db_session
from webapp.models import User

user = Blueprint('user', __name__,
                        template_folder='templates')

@user.route('/login', methods=['GET', 'POST'])
def login():

    if 'POST' == request.method:
        username = request.form['username']
        password = request.form['password']
        if user_login(username,password):
            session['username'] = request.form['username']
            # return redirect(url_for('home',username=username))
            flash(u'登录成功！')
            resp = make_response(redirect(url_for('home')))
            resp.set_cookie('username', username)
            print(username)
        else:
            flash(u'用户名或密码错误！')
            return redirect(url_for('user.login'))
    else:
        resp = make_response(render_template('login.html'))
    return resp

@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        realname = request.form['realname']
        user = User(username, password, realname)
        user_register(user)
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('username', str(user.username))
        resp.set_cookie('id',str(user.id))
        resp.set_cookie('realname',str(user.author_name))
    else:
        resp = make_response(render_template('register.html'))
    return resp

@user.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('username')
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('username', '')
    return resp

def user_register(user):
    db_session.add(user)
    db_session.commit()

def user_login(username, password):

    hasUser = User.query.filter(User.username==username,
                                User.password==password).all()
    if hasUser:
        return True
    else:
        return False