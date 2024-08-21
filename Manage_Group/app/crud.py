from sqlalchemy.orm import Session
from passlib.context import CryptContext # passlib một thư viện hỗ trợ nhiều thuật toán mã hoá mật khẩu
import models, schemas


# Tạo đối tượng CryptContext để xử lý việc hash mật khẩu
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# CRUD functions for User model
# Tạo một user mới
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        email=user.email,
        password=hashed_password,
        userName=user.userName,
        fullName=user.fullName,
        dob=user.dob
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by id
def get_user( db:Session, id : int ):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    return db_user

# Get a user by email
def get_user_by_email(db:Session, email : str):
    return db.query(models.User).filter(models.User.email == email).first()

# Đọc nhiều users
def get_users(db:Session, skip:int = 0, limit:int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Update a user
def update_user_email(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.password = user_update.password
        db_user.userName = user_update.userName
        db_user.fullName = user_update.fullName
        db_user.dob = user_update.dob
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user



# CRUD functions for Group model
# Create a new group
def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(
        name=group.groupName,
        status=group.status
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

# Get a group by ID
def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

# Get all groups
def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).offset(skip).limit(limit).all()

# Update a group
def update_group(db: Session, group_id: int, group_update: schemas.GroupUpdate):
    db_group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if db_group:
        if group_update.groupName:
            db_group.groupName = group_update.groupName
        if group_update.status is not None:
            db_group.status = group_update.status
        db.commit()
        db.refresh(db_group)
    return db_group

# Delete a group
def delete_group(db: Session, group_id: int):
    db_group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if db_group:
        db.delete(db_group)
        db.commit()
    return db_group



# CRUD functions for Member model
# Create a new member
def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(
        userId=member.userId,
        groupId=member.groupId,
    )
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

# Get a member by ID
def get_member(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.id == member_id).first()

# Get all members by groupId
def get_members_by_group(db: Session, group_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Member).filter(models.Member.groupId == group_id).offset(skip).limit(limit).all()

# Update a member
def update_member(db: Session, member_id: int, member_update: schemas.MemberUpdate):
    db_member = db.query(models.Member).filter(models.Member.id == member_id).first()
    if db_member:
        if member_update.role is not None:
            db_member.role = member_update.role
        # if member_update.join_status is not None:
        #     db_member.join_status = member_update.join_status
        db.commit()
        db.refresh(db_member)
    return db_member

# Delete a member
def delete_member(db: Session, member_id: int):
    db_member = db.query(models.Member).filter(models.Member.id == member_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()
    return db_member



# CRUD functions for Post model
# Creat a post
def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(
        groupId=post.groupId,
        authorId=post.authorId,
        title=post.title,
        content=post.content,
        category=post.category,
        status=post.status
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Get a post by ID
def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

# Get all posts
def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()

# Update a post
def update_post(db: Session, post_id: int, post_update: schemas.PostCreate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db_post.title = post_update.title
        db_post.content = post_update.content
        db_post.category = post_update.category
        db_post.status = post_update.status
        db.commit()
        db.refresh(db_post)
    return db_post

# Delete a post
def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post


