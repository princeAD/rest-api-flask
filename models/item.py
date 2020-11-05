# import sqlite3
from db import db

from werkzeug.exceptions import PreconditionRequired
class ItemModel(db.Model):
    __tablename__ ="items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def json(self):
        return {"name": self.name, "price": self.price}
    
    @classmethod
    def find_by_name(cls,name):
        # WITHOUT USING SQLAlchemy
        # # item = next(filter(lambda x: x['name']==name, items), None)
        # # return item, 200 if item else 404
        # connection = sqlite3.connect('my_database.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(*row) #same as==> return cls(row[0], row[1])
        # else:
        #     return None

        # USING SQLAlchemy
        return cls.query.filter_by(name=name).first() # SELECT * FROM items where name = name 
                                                            # this return statement returns object ItemModel
    # def update(self):
    #     connection = sqlite3.connect('my_database.db')
    #     cursor = connection.cursor()
    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query, (self.price , self.name))
    #     connection.commit()
    #     connection.close()
    
    def save_to_db(self): 
        #def insert(self):
        # Without using SQLAlchemy
        # connection = sqlite3.connect('my_database.db')
        # cursor = connection.cursor()
        # query = "INSERT INTO items VALUES(?,?)"
        # cursor.execute(query, (self.name, self.price))
        # connection.commit()
        # connection.close()
        #with SQLAlchemy
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

