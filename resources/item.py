from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
# import sqlite3

items=[]
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
        type = float,
        required= True,
        help="This feild cannot be left blank!")
    

    @jwt_required()
    def get(self,name):
        # item = next(filter(lambda x: x['name']==name, items), None)
        # return item, 200 if item else 404
        item = ItemModel.find_by_name(name)
        if item:
            return {'item': item.json()}, 200
        else:
            return {'message':'item not found'}, 404

    


    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':"An item with name {} already exists.".format(name)}, 400
        data= Item.parser.parse_args()
        item = ItemModel(name=name, price=data['price'])
        item.save_to_db()
        return {"item": item.json()}, 201
    
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name=name)
        if item is None:
            try:
                item = ItemModel(name, data['price'])
            except:
                return {"message":"An error occured inserting the item"}, 500
        else:
            try:
                item.price = data['price']
            except:
                return {"message":"An error occured inserting the item"}, 500
        
        item.save_to_db()
        return {'item': item.json()}, 201
    

    def delete(self,name):
        # connection = sqlite3.connect("my_database.db")
        # cursor = connection.cursor()
        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))
        # connection.commit()
        # connection.close()
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': 'Item Deleted'}


class Itemlist(Resource):
    def get(self):
        # items =[]
        # connection = sqlite3.connect('my_database.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)

        # for row in result:
        #     items.append({'name': row[1], 'price': row[2]})
        
        # connection.close()
        
        #<--- alternative method -->
        # item = []
        # for i in ItemModel.query.all():
        #     item.append(i.json())
        return {"items": [item.json() for item in ItemModel.query.all()]} # list comprehension
        # return {"items": list(map(lambda x:x.json(), ItemModel.query.all() ))}
