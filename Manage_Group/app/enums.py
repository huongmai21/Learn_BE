import enum
from sqlalchemy import Enum

# Trong groups
class GroupStatus(str, Enum):
    public = "public"
    private = "private"

class RequestStatus(str,Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    

# Trong members
class MemberRole(Enum):
    admin = 1
    member = 2
    contributor = 3

class MemberStatus(str, Enum):
    invited = 1
    accepted = 2


# Trong posts
class PostStatus(str, Enum):
    only = "only"
    public = "public"
    limited = "limited"

class QueuePost(str,Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"