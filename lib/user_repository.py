from lib.user import *

class UserRepository:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def all(self):
        rows = self.database_connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row['id'], row['email'], row['username'])
            users.append(item)

        return users