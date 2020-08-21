import unittest

from deezerart.deezer.client import SearchOptions

class TestSearchOptions(unittest.TestCase):
    def test_search_options(self):
        opts = SearchOptions(artist='Metallica')
        self.assertEqual(str(opts), 'artist:"Metallica"')
