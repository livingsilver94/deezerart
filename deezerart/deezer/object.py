import enum
from typing import Any, List, Mapping

# This module is a perfect target for dataclasses.
# Picard though supports Python 3.5+, so we cannot
# use dataclasses for compatibility reasons.


class Object:
    """
    Base class from Deezer API objects.
    """

    fields: List[str]

    def __init__(self, **kwargs):
        if len(self.fields) == 0:
            raise NotImplementedError(type(self).__name__ + ' cannot have an empty field list')
        for field in self.fields:
            setattr(self, field, kwargs.get(field))

    @classmethod
    def from_json(cls, json_data: Mapping[str, Any]):
        return cls(**json_data)

    def __eq__(self, other):
        for field in self.fields:
            if getattr(self, field) != getattr(other, field):
                return False
        return True


class Artist(Object):
    """
    The Artist API object.
    """

    fields = ['name']


class CoverSize(enum.Enum):
    """
    Cover size selector.
    """

    THUMBNAIL = 'small'
    SMALL = ''
    MEDIUM = 'medium'
    BIG = 'big'
    LARGE = 'xl'


class Album(Object):
    fields = ['title', 'cover']

    def cover_url(self, cover_size: CoverSize) -> str:
        """
        Get the album cover URL based on the size wanted.
        """
        return '{}/?size={}'.format(self.cover, cover_size.value)


class Track(Object):
    """
    The Track API object.
    """

    fields = ['album', 'artist']


_available_objects = {c.__name__.lower(): c for c in Object.__subclasses__()}
