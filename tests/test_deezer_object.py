import json
import unittest

from parameterized import parameterized
from deezerart.deezer import object as deezerobj


class TestJSONParsing(unittest.TestCase):
    @parameterized.expand([
        (
            'all_fields',
            '{"title": "Good Things", "cover": "https://api.deezer.com/album/54302092/image"}',
            deezerobj.Album(title='Good Things', cover='https://api.deezer.com/album/54302092/image')
        ),
        (
            'with_none',
            '{"title": "Good Things"}',
            deezerobj.Album(title='Good Things', cover=None)
        )
    ])
    def test_album(self, _name, json_doc, expected):
        self.assertEqual(json.loads(json_doc, object_hook=deezerobj.Album.from_json), expected)
