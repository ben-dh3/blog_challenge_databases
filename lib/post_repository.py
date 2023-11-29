from lib.post import *

class PostRepository:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def all(self):
        rows = self.database_connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'], row['views'], row['user_id'])
            posts.append(item)

        return posts