import ap, unittest, flask_testing, requests, flask
from flask_testing import TestCase

class integration_test(flask_testing.LiveServerTestCase):
    def create_app(self):
        return ap.app

    # Test response code = 200
    def test_server_response_200(self):
        response = requests.get(self.get_server_url())
        self.assertEqual(response.status_code, 200)
        
    # Test render path
    def test_request_path(self):
        assert flask.request.path == '/'



if __name__ == '__main__':
    unittest.main()
    # To run unit tests: python -m tests.integration_tests 