from lib.post_repository import *
from lib.post import *

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()

    assert posts == [
        Post(1, 'Test Title', 'Test Content', 10, 1),
    ]