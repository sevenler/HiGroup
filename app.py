#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from urls import handlers
from config import TEMPLATES_DIR, STATIC_DIR, DEBUG, SERVER_ADDRESS, SERVER_PORT
from tornado.options import define, options

define("address", default=SERVER_ADDRESS, help="run on the given port", type=int)
define("port", default=SERVER_PORT, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), TEMPLATES_DIR),
            static_path=os.path.join(os.path.dirname(__file__), STATIC_DIR),
            debug=DEBUG,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
