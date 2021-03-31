import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(10), nullable=False)
    profile_photo = image_attachment (profile_photo)
    biography = Column(String(150), nullable=False)
    location = Column(String(50), nullable=False)
    highlights = Column(String(20), nullable=False)

class Profile_Photo(Base, Image):
    __tablename__ = profile_photo
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    photo = image_attachment (post_photo)
    description = Column(String(250))

class Post_Photo(Base, Image):
    __tablename__ = post_photo
    user_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post = relationship(Post)

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(String(30))
    content = Column(String(250))

class Like(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    post_id = Column(String(50))

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    followers_id = Column(String(50))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')