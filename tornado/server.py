import tornado.ioloop
import tornado.web
import tornado.httpserver

from base_handler import BaseHandler
from camera_handler import CAMERA_ObjectDetection

class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello tornado!")

def make_app():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/0/objdet", CAMERA_ObjectDetection),
    ], debug = True
    )
    return application

from constants import HTTP_PORT
def main():
    print('tornado running...')
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app, decompress_request=True)
    http_server.listen(HTTP_PORT)
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
