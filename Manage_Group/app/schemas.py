from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date
from enum import Enum
from .enums import *

class Token(BaseModel):
    access_token : str  # Chuỗi đại diện cho token truy cập được cấp phát sau khi người dùng đăng nhập thành công.
    token_type : str    # Loại của token (thường là "bearer" trong các hệ thống OAuth2)

class Tokendata(BaseModel):     # thường dùng để biểu diễn thông tin dữ liệu của một token, ví dụ như ID của người dùng mà token đại diện:
    id : Optional[int] = None 


# Voi user
class UserCreate(BaseModel):
    email : EmailStr
    password : str
    userName : str
    fullName : str
    dob : Optional[date] = None # Optional ngĩa là có thể chứa giá trị None

class UserUpdate(BaseModel):
    password : str
    userName: str
    fullName : str
    dob : Optional[date] = None 

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    userName : str
    fullName : str
    createdTime: datetime
    
    class Config:
        orm_mode = True


# Voi group

class GroupCreate(BaseModel):
    groupName: str
    status: GroupStatus = GroupStatus.public

class GroupUpdate(BaseModel):
    groupName: str
    status: GroupStatus = GroupStatus.public

class GroupResponse(BaseModel):
    id: int
    groupName: str
    createdTime: datetime
    
    class Config:
        orm_mode = True



# Voi member

class MemberCreate(BaseModel):
    userId: int
    groupId: int
    role  : MemberRole = MemberRole.member
    join_status: MemberStatus = MemberStatus.accepted

class MemberUpdate(BaseModel):
    role : MemberRole = MemberRole.member
    
class MemberResponse(BaseModel):
    id: int
    groupId: int 
    userId: int
    role : MemberRole = MemberRole.member
    join_status: MemberStatus = MemberStatus.accepted
    joinTime: datetime

    class Config:
        orm_mode = True



# Voi bai posts

class PostCreate(BaseModel):
    groupId: int
    authorId: int
    title: str
    content: str
    category: int
    status : PostStatus = PostStatus.public

class PostUpdate(BaseModel):
    title: str
    content: str
    category: int
    status : PostStatus = PostStatus.public 

class PostResponse(BaseModel):
    id: int
    groupId: int
    authorId: int
    title: str
    content: str
    category: int
    status : PostStatus = PostStatus.public 
    acceptedTime : datetime
    updatedTime : datetime

    class Config: 
        orm_mode = True # Them line nay vi khi tao 1 obj moi thi no laf kieu model,
                        # ko phai dict ma python chi lam vc voi dict nen loi



    
    

