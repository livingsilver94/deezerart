import unittest

from deezerart.deezer import obj
from parameterized import parameterized


class TestJSONParsing(unittest.TestCase):
    @parameterized.expand([
        (
            'all_fields',
            '{"title": "Good Things", "cover": "https://api.deezer.com/album/54302092/image", "type":"album"}',
            obj.Album(title='Good Things', cover='https://api.deezer.com/album/54302092/image')
        ),
        (
            'with_a_none',
            '{"title": "Good Things", "type":"album"}',
            obj.Album(title='Good Things', cover=None)
        )
    ])
    def test_album(self, _name, json_doc, expected):
        self.assertEqual(obj.parse_json(json_doc), expected)

    @parameterized.expand([
        (
            'all_fields',
            '{"name": "Metallica", "type":"artist"}',
            obj.Artist(name='Metallica')
        ),
        (
            'with_a_none',
            '{"type":"artist"}',
            obj.Artist(name=None)
        )
    ])
    def test_artist(self, _name, json_doc, expected):
        self.assertEqual(obj.parse_json(json_doc), expected)

    @parameterized.expand([
        (
            'all_fields',
            '{"artist":{"name":"Metallica", "type":"artist"},"album":{"title":"Good Things","cover":"https://api.deezer.com/album/54302092/image", "type":"album"}, "type":"track"}',
            obj.Track(artist=obj.Artist(name='Metallica'), album=obj.Album(title='Good Things', cover='https://api.deezer.com/album/54302092/image'))
        ),
        (
            'with_a_none',
            '{"album":{"title":"Good Things","cover":"https://api.deezer.com/album/54302092/image", "type":"album"}, "type":"track"}',
            obj.Track(artist=None, album=obj.Album(title='Good Things', cover='https://api.deezer.com/album/54302092/image'))
        )
    ])
    def test_track(self, _name, json_doc, expected):
        self.assertEqual(obj.parse_json(json_doc), expected)


class TestDictConversion(unittest.TestCase):
    def test_track(self):
        dct = {
            'artist': {'name': 'Aloe Blacc', 'type': 'artist'},
            'album': {'title': 'Good Things', 'cover': 'http://example.com', 'type': 'album'},
            'type': 'track'
        }
        expected = obj.Track(artist=obj.Artist(name='Aloe Blacc'),
                             album=obj.Album(title='Good Things', cover='http://example.com'))

        self.assertEqual(obj.parse_json(dct), expected)
