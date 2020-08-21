import unittest

from deezerart.deezer import object as deezerobj
from parameterized import parameterized


class TestJSONParsing(unittest.TestCase):
    @parameterized.expand([
        (
            'all_fields',
            '{"title": "Good Things", "cover": "https://api.deezer.com/album/54302092/image", "type":"album"}',
            deezerobj.Album(title='Good Things', cover='https://api.deezer.com/album/54302092/image')
        ),
        (
            'with_a_none',
            '{"title": "Good Things", "type":"album"}',
            deezerobj.Album(title='Good Things', cover=None)
        )
    ])
    def test_album(self, _name, json_doc, expected):
        self.assertEqual(deezerobj.parse_json(json_doc), expected)

    @parameterized.expand([
        (
            'all_fields',
            '{"name": "Metallica", "type":"artist"}',
            deezerobj.Artist(name='Metallica')
        ),
        (
            'with_a_none',
            '{"type":"artist"}',
            deezerobj.Artist(name=None)
        )
    ])
    def test_artist(self, _name, json_doc, expected):
        self.assertEqual(deezerobj.parse_json(json_doc), expected)

    @parameterized.expand([
        (
            'all_fields',
            '{"artist":{"name":"Metallica", "type":"artist"},"album":{"title":"Good Things","cover":"https://api.deezer.com/album/54302092/image", "type":"album"}, "type":"track"}',
            deezerobj.Track(artist=deezerobj.Artist(name='Metallica'), album=deezerobj.Album(title='Good Things', cover='https://api.deezer.com/album/54302092/image'))
        ),
        (
            'with_a_none',
            '{"album":{"title":"Good Things","cover":"https://api.deezer.com/album/54302092/image", "type":"album"}, "type":"track"}',
            deezerobj.Track(artist=None, album=deezerobj.Album(title='Good Things', cover='https://api.deezer.com/album/54302092/image'))
        )
    ])
    def test_track(self, _name, json_doc, expected):
        self.assertEqual(deezerobj.parse_json(json_doc), expected)


class TestDictConversion(unittest.TestCase):
    def test_track(self):
        dct = {
            'artist': {'name': 'Aloe Blacc', 'type': 'artist'},
            'album': {'title': 'Good Things', 'cover': 'http://example.com', 'type': 'album'},
            'type': 'track'
        }
        expected = deezerobj.Track(artist=deezerobj.Artist(name='Aloe Blacc'),
                                   album=deezerobj.Album(title='Good Things', cover='http://example.com'))

        self.assertEqual(deezerobj.parse_json(dct), expected)
