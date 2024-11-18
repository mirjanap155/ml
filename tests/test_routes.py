import unittest
from run import app

class AppTestCase(unittest.TestCase):

    # Set up the test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test valid issue (anxiety)
    def test_valid_recommendation(self):
        response = self.app.get('/recommend?issue=anxiety')
        self.assertEqual(response.status_code, 200)
        self.assertIn('anxiety', response.json['issue'])
        self.assertGreater(len(response.json['recommendations']), 0)

    # Test invalid issue (unknown)
    def test_invalid_recommendation(self):
        response = self.app.get('/recommend?issue=unknown')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)

if __name__ == "__main__":
    unittest.main()
