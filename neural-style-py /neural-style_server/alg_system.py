# coding: utf-8
from __future__ import print_function
import tensorflow as tf
from preprocessing import preprocessing_factory
import reader
import model
import time
import os,base64,cv2

import numpy as np
def decode_img(img_string):
    img_data = base64.b64decode(img_string)
    np_array = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    tmp_file ='./tmp/'+time.strftime('del_%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))+'.jpg'
    cv2.imwrite(tmp_file,img)
    return tmp_file

class alg_system:
    def __init__(self):
        self.loss_model='vgg_16'
    def infer(self,model_file,image_file):
        image_file=decode_img(image_file)
        image1 = cv2.imread(image_file)
        height = image1.shape[0]
        width = image1.shape[1]
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        print('Image size: %dx%d' % (width, height))
        with tf.Graph().as_default():
            with tf.Session(config=config).as_default() as sess:
    
                # Read image data.
                image_preprocessing_fn, _ = preprocessing_factory.get_preprocessing(
                    self.loss_model,
                    is_training=False)
                image = reader.get_image(image_file, height, width, image_preprocessing_fn)
    
                # Add batch dimension
                image = tf.expand_dims(image, 0)
    
                generated = model.net(image, training=False)
                generated = tf.cast(generated, tf.uint8)
    
                # Remove batch dimension
                generated = tf.squeeze(generated, [0])
    
                # Restore model variables.
                saver = tf.train.Saver(tf.global_variables(), write_version=tf.train.SaverDef.V1)
                sess.run([tf.global_variables_initializer(), tf.local_variables_initializer()])
                # Use absolute path
                model_file = os.path.abspath(model_file)
                saver.restore(sess, model_file)
    
                # Make sure 'generated' directory exists.
                generated_file ='./tmp/'+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))+'.jpg'
                if os.path.exists('tmp') is False:
                    os.makedirs('tmp')
    
                # Generate and write image data to file.
                with open(generated_file, 'wb') as img:
                    start_time = time.time()
                    img.write(sess.run(tf.image.encode_jpeg(generated)))
                    end_time = time.time()
                    print('Elapsed time: %fs' % (end_time - start_time))
                os.remove(image_file)
                with open(generated_file,'rb') as f:
                    style_base64=base64.b64encode(f.read())
                    s = style_base64.decode()
                    #str(style_base64, encoding = "utf8")  
            return s  