from security import authenticate, identity
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, Itemlist

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'prahanjal'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()
    # before the first request runs this function will be called and it is going
    # to run db.create_all()
    # this will create the file "sqlite:///my_database.db" as well it will 
    # create the tables in the file unless it already exists

jwt = JWT(app, authenticate, identity) # /auth


    
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')


if __name__ == "__main__": #if we import app in any other python file , it would not run app unless "python aap.py" command is given
    from db import db  # beacuse of circular import it is not imported in the top with other imports
    db.init_app(app)
    app.run(port=5000, debug = True)