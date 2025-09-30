# test_main.py
import pytest
from main import app  # Assuming main.py defines the Flask app 'app'

# Create a fixture for the test client
@pytest.fixture
def client():
    # Set the testing configuration
    app.config['TESTING'] = True
    # Create the test client
    with app.test_client() as client:
        yield client

# Test the root route '/'
def test_hello_world_endpoint(client):
    # Send a GET request to the root URL
    response = client.get('/')
    # Check if the status code is 200 OK
    assert response.status_code == 200
    # Check if the response data contains the expected string
    assert b"Hello, World! The CI/CD Pipeline worked! Version 2.0" in response.data