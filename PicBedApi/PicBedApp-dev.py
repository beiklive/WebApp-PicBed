import tornado.ioloop
import tornado.web
import json
import os,base64
import uuid

import ImageModule
import configRead
import TokenGen

def WriteBackJson(data, status, sign):
    ReturnDict = {"data": data, "status" : status, "sign": sign}
    return json.dumps(ReturnDict)


def ReadConfig(index):
    if index == 1:
        return configRead.ReadElem("Server", "port")
    if index == 2:
        return configRead.ReadElem("Admin", "Passwd")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./index.html")

class StaticFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class RedirectRequestHandler(tornado.web.RequestHandler):
    def get(self):
        Retype = self.get_argument("type")
        if Retype == 'random':
            url = ImageModule.GetRandom()
            print(url)
        self.redirect(url)

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
        temp = TokenGen.check_token(self.get_argument("sign"))
        if temp == TokenGen.ERROR_CODE:
            self.write(WriteBackJson("error", "error", "error"))
        elif temp == TokenGen.EXPIRE_CODE:
            self.write(WriteBackJson("error", "expire", "error"))
        else:
            Imgtype = self.get_argument("type")
            get = self.get_argument("base64file")
            name = str(uuid.uuid4())+'.'+ str(Imgtype)
            ImageModule.SaveImg("./imgSource/", name, get)
            # 储存略缩图
            ImageModule.SaveThumb("./imgSource/", "./thumbnail/", name)
            self.write(WriteBackJson("complete", "success", temp))

class ImgRequestHandler(tornado.web.RequestHandler):
        # 允许跨域
    def set_default_headers(self):
        # print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE, PUT')
        self.set_header("Access-Control-Allow-Headers", "token, content-type, user-token")
    def get(self):
        m_cmd = self.get_argument("cmd")
        print("get request: " + m_cmd)

        if m_cmd == "ImgLoad":
            ImageModule.ImgLoadCMD(self)
        elif m_cmd == "Login":
            pw = self.get_argument("pw")
            if pw == ReadConfig(2):
                data = "<li class=\"nav-item\"><a class=\"nav-link text-muted\" href=\"#\" data-bs-toggle=\"modal\" data-bs-target=\"#myModal\"><i class=\"fa fa-cloud-upload\"></i>上传</a></li>"
                self.write(WriteBackJson(data, "success", TokenGen.get_token()))
            else:
                self.write(WriteBackJson("error", "error", "error"))
        elif m_cmd == "Config":
            self.write(json.dumps(configRead.PageConfig()))
        elif m_cmd == "ImgDelete":
            temp = TokenGen.check_token(self.get_argument("sign"))
            if temp == TokenGen.ERROR_CODE:
                self.write(WriteBackJson("error", "error", "error"))
            elif temp == TokenGen.EXPIRE_CODE:
                self.write(WriteBackJson("error", "expire", "error"))
            else:
                self.write(WriteBackJson(ImageModule.ImgDeleteCMD(self), "success", temp))

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
        (r"/redirect",RedirectRequestHandler),
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
        ImageModule.PreLoad()
        app = make_app()
        port = ReadConfig(1)
        app.listen(port)
        print("please open url :  localhost:" + str(port))
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nSee You !!!")