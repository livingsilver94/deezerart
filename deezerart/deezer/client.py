import json
from functools import partial
from typing import Callable, List, NamedTuple, Optional, TypeVar

from picard.webservice import WebService
from PyQt5.QtNetwork import QNetworkReply

from deezerart.deezer import obj

DEEZER_HOST = 'api.deezer.com'
DEEZER_PORT = 443


T = TypeVar('T', bound=obj.Object)
SearchCallback = Callable[[Optional[List[T]], Optional[QNetworkReply.NetworkError]], None]


class SearchOptions(NamedTuple('SearchOptions', [('artist', str), ('album', str), ('track', str), ('label', str)])):
    """
    Options for the advanced search.
    """

    def __str__(self):
        options = ['{}:"{}"'.format(k, v) for k, v in self._asdict().items() if v]
        return ' '.join(options)


# Python 3.5 cannot set defaults values in an othodox way.
SearchOptions.__new__.__defaults__ = ('',) * len(SearchOptions._fields)


class Client:
    def __init__(self, webservice: WebService):
        self.webservice = webservice
        self._get = partial(self.webservice.get, DEEZER_HOST, DEEZER_PORT)

    def advanced_search(self, options: SearchOptions, callback: SearchCallback[obj.Object]):
        path = '/search?q='

        def handler(document: str, _reply: QNetworkReply, error: Optional[QNetworkReply.NetworkError]):
            if error:
                callback(None, error)
                return
            parsed_doc = json.loads(document)
            callback([obj.parse_json(dct) for dct in parsed_doc['data']], error)

        self._get(path + str(options),
                  handler=handler,
                  parse_response_type=None)
