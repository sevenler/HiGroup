from base import BaseView
from core.logic import Group


class JoinView(BaseView):
    def post(self, group_id):
        me = self.get_currenct_user()
        group = Group(group_id)

        message = '加入失败，请重试！'
        if group.join(me) == True:
            message = '加入小组%s成功'%group.name

        self.message(message, '/')
