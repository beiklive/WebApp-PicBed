import os
import tornado.web
import tornado.ioloop
from utils import RouterHandle   


def make_app():
    return tornado.web.Application([
        (r"/api", RouterHandle.APIHandler),
        (r"/404", RouterHandle.NotFound404Handler),
        # 静态文件路由必须放在最后，否则会拦截所有请求
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "web/dist", "default_filename": "index.html"}),
    ])

if __name__ == "__main__":
    app = make_app()
    print("Server started at http://localhost:8961")
    app.listen(8961)
    tornado.ioloop.IOLoop.current().start()
