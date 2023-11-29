from lib.post import *
# id title content views user_id
def test_post_constructs():
    post = Post(1, "Test Post", "Test Content", 10, 1)
    assert post.id == 1
    assert post.title == "Test Post"
    assert post.content == "Test Content"
    assert post.views == 10
    assert post.user_id == 1

def test_posts_format_nicely():
    post = Post(1, "Test Post", "Test Content", 10, 1)
    assert str(post) == "Post(1, Test Post, Test Content, 10, 1)"

def test_posts_are_equal():
    post1 = Post(1, "Test Post", "Test Content", 10, 1)
    post2 = Post(1, "Test Post", "Test Content", 10, 1)
    assert post1 == post2