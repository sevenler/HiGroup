from base import BaseObject

class User(BaseObject):
    def __init__(self, pk, model=None):
        super(User, self).__init__(pk)
        self._model = model

    def info(self):
        super_info = super(User, self).info()
        model = self._model
        super_info.extend({
            'name': model.name
        })
        return super_info

    @property
    def name(self):
        return self._model.name

    @classmethod
    def sign_up(cls, **kwargs):
        pass

    @classmethod
    def sign_in(cls, email, password):
        pass
