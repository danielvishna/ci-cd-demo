from main import greet

def test_greet():
    assert greet() == "Hello from CI/CD!"


def test_greet1():
    assert greet() == "Something wrong!"  # This will FAIL
