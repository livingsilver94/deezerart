
from typing import List, Optional

from picard import log
from picard.coverart import providers
from picard.coverart.image import CoverArtImage
from PyQt5.QtNetwork import QNetworkReply

from .deezer import Client, SearchOptions, obj


class Provider(providers.CoverArtProvider):
    NAME = 'Deezer'

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
