from main import greet, add

def test_greet():
    assert greet() == "Hello from CI/CD!"

def test_add():
    assert add(2, 3) == 5  # This should pass

    # Try this next to make it fail and see behavior:
    # assert add(2, 3) == 6  # This will FAIL
