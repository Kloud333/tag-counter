import unittest
from counter.services.parser import Parser


class TestsParser(unittest.TestCase):

    def test_count_tags_good_response(self):
        parser = Parser('<html><div></div></html>')
        self.assertEqual({'html': 1, 'div': 1}, parser.count_tags())

    def test_count_tags_empty_response(self):
        parser = Parser('')
        self.assertEqual({'error': 'No tags found'}, parser.count_tags())

    def test_count_tags_bad_url_response(self):
        parser = Parser({'error': 'Invalid URL'})
        self.assertEqual({'error': 'Invalid URL'}, parser.count_tags())


if __name__ == '__main__':
    unittest.main()
