PLUGIN_NAME = "Deezer cover art"
PLUGIN_AUTHOR = "Fabio Forni <livingsilver94>"
PLUGIN_DESCRIPTION = "Fetch cover arts from Deezer"
PLUGIN_VERSION = '1.0.0'
PLUGIN_API_VERSIONS = ['2.2']
PLUGIN_LICENSE = "GPL-3.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"

from picard.coverart import providers
from deezerart.deezer import Client


class Provider(providers.CoverArtProvider):
    def __init__(self, coverart):
        super().__init__(coverart)
        self.client = Client(self.album.tagger.webservice)

    def queue_images(self):
        pass


providers.register_cover_art_provider(Provider)
