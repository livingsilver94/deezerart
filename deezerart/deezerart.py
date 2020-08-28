PLUGIN_NAME = "Deezer cover art"
PLUGIN_AUTHOR = "Fabio Forni <livingsilver94>"
PLUGIN_DESCRIPTION = "Fetch cover arts from Deezer"
PLUGIN_VERSION = '1.0.0'
PLUGIN_API_VERSIONS = ['2.2']
PLUGIN_LICENSE = "GPL-3.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"


from typing import List, Optional

from picard import log
from picard.coverart import providers
from picard.coverart.image import CoverArtImage
from PyQt5.QtNetwork import QNetworkReply

from .deezer import Client, SearchOptions, obj


class Provider(providers.CoverArtProvider):
    def __init__(self, coverart):
        super().__init__(coverart)
        self.client = Client(self.album.tagger.webservice)

    def queue_images(self):
        search_opts = SearchOptions(title=self.metadata['artist'], album=self.metadata['musicbrainz_releasegroupid'])
        self.client.advanced_search(search_opts, self._search_callback)
        return self.WAIT

    def _search_callback(self, results: Optional[List[obj.Object]], error: Optional[QNetworkReply.NetworkError]):
        try:
            if error or (results is None or len(results) == 0):
                log.error("Deezerart: could not fetch search results: %s", error or "empty list")
                return
            for result in results:
                if not isinstance(result, obj.Track):
                    continue
                album = self.metadata['musicbrainz_releasegroupid']
                artist = self.metadata['artist']
                if result.artist.name != artist and result.album.title != album:
                    continue
                self.queue_put(CoverArtImage(result.album.cover_url(obj.CoverSize.BIG)))
        finally:
            self.next_in_queue()


providers.register_cover_art_provider(Provider)
