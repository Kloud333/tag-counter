import unittest
from counter.services.aliases.aliases import Aliases
from counter.services.parser import Parser
from unittest.mock import MagicMock


class TestsAliases(unittest.TestCase):

    def test_get_url_response(self):
        alias = Aliases()
        alias.load_yaml = MagicMock(return_value={'ggl': 'google.com', 'ydx': 'yandex.ru', 'sof': 'stackoverflow.com'})

        self.assertEqual('https://google.com', alias.get_url('ggl'))
        self.assertEqual('https://google.com', alias.get_url('google.com'))
        self.assertEqual('https://github.com', alias.get_url('github.com'))
        self.assertEqual('https://github.com', alias.get_url('https://github.com'))


if __name__ == '__main__':
    unittest.main()
