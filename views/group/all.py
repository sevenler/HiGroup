from base import BaseView


class AllView(BaseView):
    def get(self):
        all_group_obj = Group.filter()
        group_map_list = []
        for group in all_group_obj:
            group_map_list.append(group.info())
        self.render("index.html", group_map_list)
