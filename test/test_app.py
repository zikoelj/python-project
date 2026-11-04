from app import index, add


def test_index():
    assert index() == "Hello, world!"


def test_add():
    assert add(2, 3) == "5"
