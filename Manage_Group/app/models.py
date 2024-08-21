from .database import Base
from sqlalchemy import Column, Integer, String, Enum, Boolean, Date, ForeignKey, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from .enums import *
from enum import Enum

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True) # index: Tạo chỉ mục trên cột để tăng tốc độ truy vấn.
    password = Column(String, nullable=False)
    userName = Column(String, nullable=False,unique=True,index=True)
    fullName = Column(String, nullable=False)
    dob = Column(Date, nullable=True)
    createTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    # posts = relationship("Post", back_populates="owner")


class Group(Base):
    __tablename__ = "groups_"

    id = Column(Integer, primary_key=True, nullable=False)
    groupName = Column(String, nullable=False,unique=True, index=True)
    status = Column(GroupStatus,nullable=False)
    creatTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    groupId = Column(Integer, ForeignKey("groups_.id", ondelete="CASCADE"), nullable=False)
    

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer,primary_key=True,nullable=False)
    status = Column(Enum(RequestStatus),nullable=False,default=RequestStatus.pending)
    requestTime = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

    user_request = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    group_request = Column(Integer, ForeignKey("groups_.id", ondelete="CASCADE"), nullable=False)


class Role(Base):
    __tablename__ = "role_m"
    
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    roleName = Column(Enum(MemberRole),nullable=False)


class Status(Base):
    __tablename__ = "join_status"

    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    statusName = Column(Enum(MemberStatus),nullable=False)


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, nullable=False)
    joinTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    userId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    groupId = Column(Integer, ForeignKey("groups_.id", ondelete="CASCADE"), nullable=False)
    role = Column(Integer,ForeignKey("role_m.id",ondelete="CASCADE"),nullable=False)
    join_status = Column(Integer,ForeignKey("join_status.id",ondelete="CASCADE"),nullable=False)



class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    category = Column(String,nullable=False)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    status = Column(Enum(PostStatus), nullable=False, default=PostStatus.public)
    acceptTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updateTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    groupId = Column(Integer, ForeignKey("groups_.id", ondelete="CASCADE"), nullable=True)
    authorId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = Column(Integer,ForeignKey("categories.id",ondelete="CASCADE"), nullable=False)

    #owner = relationship("User",back_populates="posts")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    createTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    postId = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    userId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


class Icon(Base):
    __table__ = "icons"
   
    id = Column(Integer,primary_key=True,autoincrement=True, nullable=False)
    icon = Column(String,nullable=False)


class React(Base):
    __tablename__ = "reacts"

    id = Column(Integer, primary_key=True, nullable=False)
    createTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    postId = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    userId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    icon = Column(Integer,ForeignKey("icons.id", ondelete="CASCADE"),nullable=False)    


class QueuePost(Base):
    __table__ = "queue_post"

    id = Column(Integer, primary_key=True, nullable=False)
    status = Column(Enum(QueuePost), nullable=False, default=QueuePost.pending)
    createTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    postId = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
