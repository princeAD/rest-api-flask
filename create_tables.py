# import sqlite3

# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)

# query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
# cursor.execute(query)

# connection.commit()
# connection.close()
# we can create files and tables with sqlalchemy ...