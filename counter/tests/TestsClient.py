import unittest
from counter.services.client import Client


class TestsClient(unittest.TestCase):

    def test_get_good_response(self):
        client = Client('https://google.com')
        self.assertTrue(type(client.get_content()) == str)

    def test_get_bad_response_invalid_url(self):
        client = Client('bad-url')
        self.assertEqual({'error': 'Invalid URL'}, client.get_content())

    def test_get_bad_response_connection_problems(self):
        client = Client('https://bad-url.com')
        self.assertEqual({'error': 'Connection problems'}, client.get_content())


if __name__ == '__main__':
    unittest.main()
