
PLUGIN_NAME = "Deezer cover art"
PLUGIN_AUTHOR = "Fabio Forni <livingsilver94>"
PLUGIN_DESCRIPTION = "Fetch cover arts from Deezer"
PLUGIN_VERSION = '1.0.0'
PLUGIN_API_VERSIONS = ['2.2', '2.3', '2.4']
PLUGIN_LICENSE = "GPL-3.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"

from typing import List, Optional

from picard.coverart import providers
from picard.coverart.image import CoverArtImage
from PyQt5.QtNetwork import QNetworkReply

from .deezer import Client, SearchOptions, obj

__version__ = PLUGIN_VERSION


class Provider(providers.CoverArtProvider):
    NAME = 'Deezer'

    def __init__(self, coverart):
        super().__init__(coverart)
        self.client = Client(self.album.tagger.webservice)

    def queue_images(self):
        search_opts = SearchOptions(artist=self.metadata['albumartist'], album=self.metadata['album'])
        self.client.advanced_search(search_opts, self._search_callback)

        self.album._requests += 1
        return self.WAIT

    def _search_callback(self, results: List[obj.Object], error: Optional[QNetworkReply.NetworkError]):
        self.album._requests -= 1
        try:
            if error or len(results) == 0:
                self.error('Deezerart: could not fetch search results: {}'.format(error or "empty list"))
                return
            artist = self.metadata['albumartist']
            album = self.metadata['album']
            for result in results:
                if not isinstance(result, obj.Track):
                    continue
                if result.artist.name != artist and result.album.title != album:
                    continue
                self.queue_put(CoverArtImage(result.album.cover_url(obj.CoverSize.BIG)))
                break
        finally:
            self.next_in_queue()


providers.register_cover_art_provider(Provider)
