from base import BaseObject
from core.models import session
from core.models import User as UserModel


class User(BaseObject):
    def __init__(self, pk, model=None):
        super(User, self).__init__(pk)
        self._model = model

    def info(self):
        super_info = super(User, self).info()
        model = self._model
        super_info.update({
            'name': model.name,
            'avatar': model.avatar_url
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

    @classmethod
    def filter(cls, **kwargs):
        user_model_list = session.query(UserModel).filter_by(**kwargs).all()
        user_object_list = []
        for item in user_model_list:
            user_object_list.append(cls(item.id, model=item))
        return user_object_list
