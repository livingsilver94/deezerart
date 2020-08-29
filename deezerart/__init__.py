PLUGIN_NAME = "Deezer cover art"
PLUGIN_AUTHOR = "Fabio Forni <livingsilver94>"
PLUGIN_DESCRIPTION = "Fetch cover arts from Deezer"
PLUGIN_VERSION = '1.0.0'
PLUGIN_API_VERSIONS = ['2.2', '2.3', '2.4']
PLUGIN_LICENSE = "GPL-3.0-or-later"
PLUGIN_LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"

from picard.coverart import providers

from .provider import Provider

__version__ = PLUGIN_VERSION

providers.register_cover_art_provider(Provider)
