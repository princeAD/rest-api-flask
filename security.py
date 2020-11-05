from models.user import UserModel
from werkzeug.security import safe_str_cmp
# users =[
#     UserModel(1, 'bob', 'asdf')
# ]

# username_mapping = {u.username: u for u in users} find_by_userid does same thing with the data in the database 


# userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(userid= user_id)
