import tornado.web
import tornado.ioloop
from . import ApiHandle

'''
API Command define
1 - request for data
2 - 
'''

class APIHandler(tornado.web.RequestHandler):
    def get(self):
        # 获取请求参数
        # print(self.get_query_argument("Command"))
        ApiHandle.ApiHandle().Process(self)
        

class NotFound404Handler(tornado.web.RequestHandler):
    def get(self):
        print("NotFound404Handler")
        self.write("Hello, NotFound404Handler")



class PhotosHandler(tornado.web.RequestHandler):
    def get(self, album_id=None, photo_id=None):
        if album_id and photo_id:
            self.write(f"Showing photo with ID {photo_id} from album with ID {album_id}")
        elif album_id:
            self.write(f"Showing all photos from album with ID {album_id}")
        else:
            self.write("Invalid URL")

class AlbumsHandler(tornado.web.RequestHandler):
    def get(self, album_id=None):
        if album_id:
            self.write(f"Showing album with ID {album_id}")
        else:
            self.write("Showing all albums")