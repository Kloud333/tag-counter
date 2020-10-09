import unittest
from counter.services.storage import Storage


class TestsAliases(unittest.TestCase):

    def test_storage_response(self):
        with Storage() as storage:
            storage.save_tags('https://google.com', {'html': 1, 'div': 2})
            results = storage.get_tags('https://google.com')

        self.assertEqual({'html': 1, 'div': 2}, results)


if __name__ == '__main__':
    unittest.main()
