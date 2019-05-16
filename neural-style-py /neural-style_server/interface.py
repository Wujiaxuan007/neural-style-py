import os
from alg_system import *
def neural_style_process(model_file,image_file,obj):
    respones_dict = {}
    model_file=".\\models\\" + model_file +".ckpt-done"
    try:
        result = obj.infer(model_file,image_file)
        respones_dict['content_image_base64']=result
        
    except Exception as e:
        print("get error:")
        print(e)
        respones_dict = {'error_code':1002}
    return respones_dict
 
    



