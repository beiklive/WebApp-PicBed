import os
import tornado.web
import tornado.ioloop
from utils import RouterHandle   


def make_app():
    return tornado.web.Application([
    # 用户登录路由: 处理用户登录请求 
        # GET请求示例路由：http://localhost:8961/api/login
        # POST请求示例路由：http://localhost:8961/api/login
        (r"/api/login", RouterHandle.LoginHandler),
    # 用户注册路由: 处理用户注册请求 
        # GET请求示例路由：http://localhost:8961/api/register
        # POST请求示例路由：http://localhost:8961/api/register
        (r"/api/register", RouterHandle.RegisterHandler),
    # 获取特定相册中的特定照片或所有照片
        # GET请求示例路由：http://localhost:8961/api/albums/123/photos/456
        # POST请求示例路由：http://localhost:8961/api/albums/123/photos
        # PUT请求示例路由：http://localhost:8961/api/albums/123/photos/456
        # DELETE请求示例路由：http://localhost:8961/api/albums/123/photos/456
        (r"/api/albums/(\d+)/photos/(\d+)", RouterHandle.PhotosHandler),
    # 获取特定相册中的所有照片
        # GET请求示例路由：http://localhost:8961/api/albums/123/photos
        # POST请求示例路由：http://localhost:8961/api/albums/123/photos
        # PUT请求示例路由：http://localhost:8961/api/albums/123/photos
        # DELETE请求示例路由：http://localhost:8961/api/albums/123/photos
        (r"/api/albums/(\d+)/photos", RouterHandle.PhotosHandler),
    # 获取特定相册信息或所有相册信息
        # GET请求示例路由：http://localhost:8961/api/albums/123
        # POST请求示例路由：http://localhost:8961/api/albums
        # PUT请求示例路由：http://localhost:8961/api/albums/123
        # DELETE请求示例路由：http://localhost:8961/api/albums/123
        (r"/api/albums/(\d+)?", RouterHandle.AlbumsHandler),
    # 获取所有相册信息
        # GET请求示例路由：http://localhost:8961/api/albums
        # POST请求示例路由：http://localhost:8961/api/albums
        # PUT请求示例路由：http://localhost:8961/api/albums
        # DELETE请求示例路由：http://localhost:8961/api/albums
        (r"/api/albums", RouterHandle.AlbumsHandler),
        # (r"/404", RouterHandle.NotFound404Handler),
        # 静态文件路由必须放在最后，否则会拦截所有请求
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "web/dist", "default_filename": "index.html"}),
    ])

if __name__ == "__main__":
    app = make_app()
    print("Server started at http://localhost:8961")
    app.listen(8961)
    tornado.ioloop.IOLoop.current().start()
