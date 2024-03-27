import tornado.web
import tornado.ioloop

'''
API Command define
1 - request for data
2 - 
'''

class APIHandler(tornado.web.RequestHandler):
    def get(self):
        # 获取请求参数
        print(self.get_query_argument("Command"))
        

class NotFound404Handler(tornado.web.RequestHandler):
    def get(self):
        print("NotFound404Handler")
        self.write("Hello, NotFound404Handler")
        