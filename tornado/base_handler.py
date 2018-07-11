import tornado.httpserver
import time

class BaseHandler(tornado.web.RequestHandler):
    AllowHeaders = set(['X-Requested-With', 'Ng-Path', 'Ak-Admin-Skey', 'Ak-Token'])

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT")
        self.set_header("Access-Control-Allow-Headers", ",".join(hd for hd in BaseHandler.AllowHeaders))
    def options(self):
        self.set_status(204)
        self.finish()

    @staticmethod
    def success_ret():
        t = int(time.time() * 1000)
        ret = {"success": "true", "sysTime": t}
        return ret

    @staticmethod
    def success_ret_with_data(data):
        ret = BaseHandler.success_ret()
        ret["data"] = data
        return ret

    @staticmethod
    def error_ret():
        t = int(time.time() * 1000)
        ret = {"success": "false", "sysTime": t}
        return ret
