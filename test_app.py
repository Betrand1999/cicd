# test_app.py
import unittest
from hello_world_app.app import app  # Import the Flask app from app.py

class FlaskAppTest(unittest.TestCase):
    # Set up the test client before each test
    def setUp(self):
        self.app = app.test_client()  # Create a test client instance
        self.app.testing = True  # Set the app to testing mode

    # Test case to check if the home page loads successfully
    def test_home_page(self):
        response = self.app.get('/')  # Make a GET request to the home page
        self.assertEqual(response.status_code, 200)  # Check that the status code is 200
        self.assertIn(b"Hello, World!", response.data)  # Check that the response contains "Hello, World!"

    # Additional test cases can go here if necessary

if __name__ == '__main__':
    unittest.main()  # Run the tests