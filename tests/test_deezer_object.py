import json
import unittest

from deezerart.deezer import object as deezerobj


class TestJSONParsing(unittest.TestCase):
    def test_album(self):
        test_table = [
            {'json': '{"title": "Good Things", "cover": "https://api.deezer.com/album/54302092/image"}',
             'expected': deezerobj.Album(title='Good Things', cover='https://api.deezer.com/album/54302092/image')},
            {'json': '{"title": "Good Things"}',
             'expected': deezerobj.Album(title='Good Things', cover=None)},
        ]
        for test in test_table:
            json_obj = json.loads(test['json'], object_hook=deezerobj.Album.from_json)
            self.assertEqual(json_obj, test['expected'])
