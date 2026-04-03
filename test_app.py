import pytest
from app import app

# This creates a virtual web browser for our tests to use
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test 1: Testing the Web Page
def test_home_page(client):
    response = client.get("/")
    
    # Did the page load without crashing?
    assert response.status_code == 200
    
    # We don't check the whole HTML. We just check if our key text is IN the HTML.
    assert b"<h1>Welcome to the Real World!</h1>" in response.data
    assert b"<title>My Awesome Site</title>" in response.data

# Test 2: Testing User Interaction (Form Submission)
def test_form_submission(client):
    # We simulate a user typing "Alice" and hitting submit (POST request)
    response = client.post("/submit", data={"username": "Alice"})
    
    # Did it process successfully?
    assert response.status_code == 200
    
    # Did it return the customized greeting?
    assert b"Thank you for logging in, Alice!" in response.data