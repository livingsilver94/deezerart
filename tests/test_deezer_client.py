import unittest

from deezerart.deezer.client import Client, SearchOptions
from parameterized import parameterized


class TestSearchOptions(unittest.TestCase):
    def test_search_options(self):
        opts = SearchOptions(artist='Metallica')
        self.assertEqual(str(opts), 'artist:"Metallica"')

    @parameterized.expand([
        ('www_deezer_no_language', 'http://www.deezer.com/track/123', 'http://api.deezer.com/track/123'),
        ('www_deezer_with_language', 'http://www.deezer.com/us/track/123', 'http://api.deezer.com/track/123'),
        ('api_deezer_no_language', 'http://api.deezer.com/track/123', 'http://api.deezer.com/track/123'),
        ('api_deezer_with_language', 'http://api.deezer.com/us/track/123', 'http://api.deezer.com/track/123'),
    ])
    def test_api_url(self, _name, orig_url: str, api_url: str):
        url = Client.api_url(orig_url)
        self.assertEqual(url, api_url)
