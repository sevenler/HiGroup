from base import BaseView
from core import Group


class CreateView(BaseView):
    def get(self):
        self.render("group/create.html",)

    def post(self):
        title = self.get_argument('title', None)
        description = self.get_argument('description', None)
        max_partner = self.get_argument('max_partner', None)
        created_user = self.get_current_user()
        group_dict = {
            'title': title,
            'description': description,
            'max_partner': max_partner,
            'created_user_id': created_user.id,
        }
        group_obj = Group.create(**group_dict)
        message = '创建小组%s成功！'%group_obj.info()['title']
        self.message(message, '/')
