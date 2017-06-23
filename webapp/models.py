from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship, query

from webapp.database import Base, db_session


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50), unique=False)
    author_name = Column(String(50), unique=False)

    def __init__(self, name, password, author_name):
        self.username = name
        self.password = password
        self.author_name = author_name

    def __repr__(self):
        return '<User %r>' % (self.username)

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=False)
    content = Column(String(150), unique=False)
    category_name = Column(String(50), unique=False)
    category_id =Column(String(150), ForeignKey('blog_category.id'), index=True, nullable=False)
    img = Column(String(150), unique=False)
    author = Column(String(150), unique=False)
    authorid = Column(String(150), ForeignKey('users.id'), index=True, nullable=False)
    count_like = Column(Integer, unique=False)
    count_scan = Column(Integer, unique=False)
    # count_comments=0;
    count_comments = Column(Integer, unique=False)
    comments_list = relationship('Comment',order_by='Comment.blog_id')

    def __init__(self, title, content, category_id,category_name='',
                 img='',author='',authorid='', count_like=0, count_scan=0, count_comments=0):
        self.title = title
        self.content = content
        self.category_id = category_id
        self.category_name = category_name
        self.img = img
        self.author = author
        self.authorid= authorid
        self.count_like = count_like
        self.count_scan = count_scan
        self.count_comments = count_comments

    def __repr__(self):
        return '<Blog %r>' % (self.title)

    def query_blog(self,id):
        blog = Blog.query.filter(Blog.id==id).first()
        return blog

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    username = Column(String(50))
    content = Column(String(150), unique=False)
    blog_id = Column(Integer, ForeignKey('blogs.id'), index=True, nullable=False)

    def __init__(self,userid, username, content, blog_id):
        self.userid = userid
        self.content = content
        self.username = username
        self.blog_id = blog_id


class Blog_category(Base):
    __tablename__ = 'blog_category'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(50))
    category_degree = Column(Integer)
    category_parent = Column(Integer)
    blog_list = relationship('Blog',order_by='Blog.category_id')
    category_child =[]
    def __init__(self,category_name, category_degree, category_parent):
        self.category_name = category_name
        self.category_degree = category_degree
        self.category_parent = category_parent

    def get_category_child(self):
        return db_session.query(Blog_category).filter(Blog_category.category_parent==self.id).all()


def get_blog_category():
    category = Blog_category.query.filter(Blog_category.category_degree == 1).all()
    if category:
        categorys = []
        for c in category:
            c.category_child = c.get_category_child()
            categorys.append(c)
    return categorys