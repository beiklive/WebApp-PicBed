import tornado.web
import tornado.ioloop

'''
API Command define
1 - request for data
2 - 
'''

# # 重写 404 
# class CustomApplication(tornado.web.Application):
#     def write_error(self, status_code, **kwargs):
#         if status_code == 404:
#             self.redirect("/404")
#         else:
#             super().write_error(status_code, **kwargs)


# class NotFound404Handler(tornado.web.RequestHandler):
#     def get(self):
#         self.set_status(404)
#         self.write("404 - Page Not Found")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")  # 渲染登录页面

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        # 在这里处理登录逻辑，验证用户名和密码

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")  # 渲染注册页面

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        # 在这里处理注册逻辑，创建新用户




class PhotosHandler(tornado.web.RequestHandler):
    def get(self, album_id=None, photo_id=None):
        if album_id and photo_id:
            self.write(f"Showing photo with ID {photo_id} from album with ID {album_id}")
        elif album_id:
            self.write(f"Showing all photos from album with ID {album_id}")
        else:
            self.write("Invalid URL")

    def post(self, album_id=None, photo_id=None):
        self.write("Creating a new photo")

    def put(self, album_id=None, photo_id=None):
        if album_id and photo_id:
            self.write(f"Updating photo with ID {photo_id} from album with ID {album_id}")
        else:
            self.write("Invalid URL")

    def delete(self, album_id=None, photo_id=None):
        if album_id and photo_id:
            self.write(f"Deleting photo with ID {photo_id} from album with ID {album_id}")
        else:
            self.write("Invalid URL")

class AlbumsHandler(tornado.web.RequestHandler):
    def get(self, album_id=None):
        if album_id:
            self.write(f"Showing album with ID {album_id}")
        else:
            self.write("Showing all albums")

    def post(self, album_id=None):
        self.write("Creating a new album")

    def put(self, album_id=None):
        if album_id:
            self.write(f"Updating album with ID {album_id}")
        else:
            self.write("Invalid URL")

    def delete(self, album_id=None):
        if album_id:
            self.write(f"Deleting album with ID {album_id}")
        else:
            self.write("Invalid URL")