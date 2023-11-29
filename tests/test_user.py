from lib.user import *
# id username email
def test_user_constructs():
    user = User(1, "Test Email", "Test Username")
    assert user.id == 1
    assert user.email == "Test Email"
    assert user.username == "Test Username"


def test_users_format_nicely():
    user = User(1, "Test Email", "Test Username")
    assert str(user) == "User(1, Test Email, Test Username)"

def test_users_are_equal():
    user1 = User(1, "Test Email", "Test Username")
    user2 = User(1, "Test Email", "Test Username")
    assert user1 == user2