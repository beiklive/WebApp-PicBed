import tornado.ioloop
import tornado.web
import json
import os,base64
import uuid

import ImageModule


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./index.html")

class StaticFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ImgUploadHandler(tornado.web.RequestHandler):
    # 允许跨域
    def set_default_headers(self):
        # print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
        self.set_header("Access-Control-Allow-Headers", "token, content-type, user-token")
    def get(self):
        print("Hello, world")
    def post(self):
        Imgtype = self.get_argument("type")
        get = self.get_argument("base64file")
        name = str(uuid.uuid4())+'.'+ str(Imgtype)
        ImageModule.SaveImg("./imgSource/", name, get)
        # 储存略缩图
        ImageModule.SaveThumb("./imgSource/", "./thumbnail/", name)

        self.write("complete")
        
class ImgRequestHandler(tornado.web.RequestHandler):
        # 允许跨域
    def set_default_headers(self):
        # print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
        self.set_header("Access-Control-Allow-Headers", "token, content-type, user-token")
    def get(self):
        m_cmd = self.get_argument("cmd")
        print("get tequest: " + m_cmd)

        if m_cmd == "ImgLoad":
            print("get tequest: " + m_cmd)
            ImageModule.ImgLoadCMD(self)

def make_app():
    settings = {
        'debug' : True,         # 修改源文件后程序自动重启
        "img_path": os.path.join(os.path.dirname(__file__), "imgSource"),        # 图片路由
        "thumb_path": os.path.join(os.path.dirname(__file__), "thumbnail"),     #略缩图路由
        "static_path": os.path.join(os.path.dirname(__file__), "templates"),        # 静态文件目录， 储存html的CSS和js
        "template_path" : os.path.join(os.path.dirname(__file__), "templates"),        # 储存html模板
    }
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ImgUpload", ImgUploadHandler),
        (r"/ImgRequest",ImgRequestHandler),
        (r"/img/(.*)$", tornado.web.StaticFileHandler, dict(path=settings['img_path'])),
        (r"/thumb/(.*)$", tornado.web.StaticFileHandler, dict(path=settings['thumb_path'])),
    ],
    **settings
    )

def CheckDirFun(path, type):
    isExists=os.path.exists(path)
    if not isExists:
        if type == "file":
            f = open('ImgData.json', 'w')
            f.write('')
            f.close()
        if type == "dir":
            os.makedirs(path) 
        isExists=os.path.exists(path)
        if not isExists:
            print(path+' 创建失败')
        else:
            print(path+' 创建成功')
    else:
        print(path+' 已存在')

def CheckDir():
    CheckDirFun("./imgSource", "dir")
    CheckDirFun("./thumbnail", "dir")
    CheckDirFun("./ImgData.json", "file")


if __name__ == "__main__":
    try:
        CheckDir()
        app = make_app()
        app.listen(6360)
        print("localhost:6360")
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nSee You !!!")