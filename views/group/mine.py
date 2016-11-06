from base import BaseView
from core import Group


class MineView(BaseView):
    def get(self):
        me = self.get_current_user()

        my_group_list = Group.filter(user_id=me.id)
        group_map_list = []
        for group in my_group_list:
            group_map_list.append.append(group.info())
        self.render("group/mine.html", group_map_list)
