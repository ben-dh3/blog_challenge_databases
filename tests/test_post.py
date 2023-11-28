from lib.post import *

def test_post_constructs():
    post = Post(1, "Test Post", "Test Content", 10, 1)
    assert post.id == 1
    assert post.title == "Test Post"
    assert post.content == "Test Content"