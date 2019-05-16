import tornado.ioloop
import tornado.web
import interface
from alg_system import *


class scanHandler(tornado.web.RequestHandler):
    def initialize(self,obj):
        self.obj = obj;
    def post(self):
        respones_dict = {};

        model_file = self.get_argument('model_file',default = "")
        image_file = self.get_argument('image_file',default = "")

        while(1):
            
            if (model_file != '')and(image_file!=''):
                respones_dict = interface.neural_style_process(model_file,image_file,self.obj)
                break
            respones_dict = {'error_code':1501}
            break;

        self.finish(respones_dict)

def make_app(obj):
    return tornado.web.Application([
        (r"/scan/", scanHandler,dict(obj=obj))
    ])
if __name__ == "__main__":
    obj = alg_system()
    app = make_app(obj)
    app.listen(16668)
    print("server start ...")
    tornado.ioloop.IOLoop.instance().start()
    