from tornado.web import url
from views import group

handlers = [
    url(r"/", group.AllView, name='index'),
    url(r"/group/create", group.CreateView, name='group.create'),
    url(r"/group/(?P<group_id>\w+)/join", group.JoinView, name='group.join'),
    url(r"/group/mine", group.MineView, name='group.mine'),
]
