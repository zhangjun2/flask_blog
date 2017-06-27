import os

from flask import Blueprint, request, url_for, render_template
from werkzeug.utils import secure_filename, redirect

from webapp.database import db_session
from webapp.models import Blog, User, Comment, Blog_category, get_blog_category

article = Blueprint('article', __name__, template_folder='templates')

@article.route('/save', methods=['GET','POST'])
def save_article():
     if request.method == 'POST':
         author = request.cookies.get('username')
         userid = request.cookies.get('id')
         title = request.form['title']
         content = request.form['content']
         type = request.form['type']
         f = request.files['fileName']
         if f:
             print(f.filename)
             filename = secure_filename(f.filename)
             file_path = 'D:\\Users\zhangjun693\PycharmProjects\webapp\webapp\\upload\\'+filename
             print(file_path)
             f.save(os.path.join(file_path))
         else:
             file_path = ''
         insert_article(userid,title,content,type,author,file_path)
         return redirect(url_for('home'))
     else:
         category = Blog_category.query.filter(Blog_category.category_degree == 2).all()
         return render_template('addblog.html',category = category)

@article.route('/detail/<article_id>')
def detail_article(article_id):
    blog = Blog.query.get(article_id)
    db_session.query(Blog).filter(Blog.id==article_id).\
        update({Blog.count_scan: Blog.count_scan+1})
    db_session.commit()
    category = get_blog_category()
    return render_template('articledetail.html', article=blog, categorys=category)

@article.route('/comment/<article_id>', methods= ['post'])
def comment(article_id):
    if request.method == 'POST':
        username = request.cookies.get('username')
        userid = request.cookies.get('userid')
        comment_content = request.form['content']
        insert_comment(userid,username,comment_content,article_id)
        return redirect(url_for('article.detail_article', article_id=article_id))


def insert_article(userid,title, content, type, author, img):
    category_id = Blog_category.query.filter(Blog_category.category_name==type).first().id
    blog = Blog(title,content,category_id)
    blog.author = author
    blog.img = img
    blog.authorid = userid
    db_session.add(blog)
    db_session.commit()

def insert_comment(userid,username, content,article_id):
    com = Comment(userid, username, content, article_id)
    db_session.add(com)
    db_session.commit()

