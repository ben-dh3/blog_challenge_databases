from lib.user_repository import *
from lib.user import *

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == [
        User(1, 'Test Email', 'Test Username'),
    ]