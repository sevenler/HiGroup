from tornado.web import url
from views import index

handlers = [
    url(r"/", index.IndexView, name='index'),
]
