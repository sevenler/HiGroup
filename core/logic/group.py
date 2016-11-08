#!/usr/bin/env python
# encoding=utf8
from base import BaseObject
from core.models import session
from core.models import Group as GroupModel
from core.models import GroupPartner as GroupPartnerModel
from core.models import GroupCheckIn as GroupCheckInModel


class Group(BaseObject):
    def __init__(self, pk, model=None):
        super(Group, self).__init__(pk)
        self._model = model

    def _confirm_model(self):
        if self._model == None:
            self._model = session.query(GroupModel).filter_by(id=self.id).first()

    def info(self):
        super_info = super(Group, self).info()

        self._confirm_model()
        model = self._model
        super_info.update({
            'title': model.title,
            'description': model.description,
            'max_partner_number': model.max_partner_number,
            'joined_partner_number': model.joined_partner_number,
            'created_user_id': model.created_user_id,
            'created_time': model.created_time,
        })
        return super_info

    @property
    def joined_partner_number(self):
        self._confirm_model()
        return self._model.joined_partner_number

    @property
    def title(self):
        self._confirm_model()
        return self._model.title

    def partners(self):
        partner_model_list = session.query(GroupPartnerModel).filter_by(group_id = self._pk).all()
        partner_map_list = []
        for partner in partner_model_list:
            partner_map_list.append({
                'user_id': partner.user_id,
            })
        return partner_map_list

    def check_in_list(self):
        check_in_model_list = session.query(GroupCheckInModel).filter_by(group_id = self._pk).all()
        check_in_map = {}
        #是否显示连续打卡天数？还是显示累计打卡天数
        for item in check_in_model_list:
            if not check_in_map.__contains__(item.user_id):
                check_in_map[item.user_id] = 0
        return check_in_map

    def join(self, user):
        exsit_partner = session.query(GroupPartnerModel).filter_by(user_id = user.id).first()
        if exsit_partner != None:
            gp = GroupPartnerModel()
            gp.user_id = user.id
            gp.group_id = self.id
            session.add(gp)
            session.flush()

            self._update(joined_partner_number=self.joined_partner_number + 1)
            return True
        else:
            return True

    def check_in(self, user):
        gci = GroupCheckInModel()
        gci.user_id = user.id
        gci.group_id = self._pk
        return True

    def _update(self, **kwargs):
        model = self._model
        if kwargs.__contains__('joined_partner_number'):
            joined_partner_number = kwargs.get('joined_partner_number', 0)
            model.joined_partner_nuber = joined_partner_number
            session.add(model)
            session.flush()

    @classmethod
    def create(cls, **kwargs):
        title = kwargs['title']
        description = kwargs.get('description', '')
        max_partner_number = kwargs.get('max_partner_number', 10)
        user_level_expectation = kwargs.get('user_level_expectation', None)
        joined_partner_number = kwargs.get('joined_partner_number', 0)
        created_user_id = kwargs.get('created_user_id', 0)

        model = GroupModel()
        model.title = title
        model.max_partner_number = max_partner_number
        model.description = description
        model.user_level_expectation = user_level_expectation
        model.joined_partner_nuber = joined_partner_number
        model.created_user_id = created_user_id

        session.add(model)
        session.flush()
        return cls(model.id, model=model)

    @classmethod
    def filter(cls, **kwargs):
        group_model_list = session.query(GroupModel).filter_by(**kwargs).all()
        group_object_list = []
        for item in group_model_list:
            group_object_list.append(cls(item.id, model=item))
        return group_object_list
