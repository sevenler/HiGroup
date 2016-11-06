from base import BaseObject


class BaseObject:
    def __init__(self):
        self._pk = pk

    @property
    def id(cls):
        return self._pk

    @classmethod
    def create(cls, **kwargs):
        pass

    @classmethod
    def filter(cls, **kwargs):
        pass
