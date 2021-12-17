

import time

import cv2
import numpy as np
from PIL import Image

from yolo import YOLO

if __name__ == "__main__":
    yolo = YOLO()
    #----------------------------------------------------------------------------------------------------------#
    #   mode: setting mode
    #   'predict' mode : predict single image

    #   'dir_predict' mode: iterate the directory and save the outcome in another directory
    #----------------------------------------------------------------------------------------------------------#
    #mode = "predict"
    mode = 'dir_predict'

    test_interval   = 100
    #-------------------------------------------------------------------------#
    #   dir_origin_path: path for the directory containint images
    #   dir_save_path: path to save image
    #   dir_origin_path and dir_save_path work only if mode='dir_predict'
    #-------------------------------------------------------------------------#
    dir_origin_path = "img"
    dir_save_path   = "img_result_save"

    if mode == "predict":

        while True:
            img = input('Input image filename:')
            try:
                image = Image.open(img)
            except:
                print('Open Error! Try again!')
                continue
            else:
                r_image = yolo.detect_image(image)
                r_image.show()



    elif mode == "dir_predict":
        import os

        from tqdm import tqdm

        img_names = os.listdir(dir_origin_path)
        for img_name in tqdm(img_names):
            if img_name.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                image_path  = os.path.join(dir_origin_path, img_name)
                image       = Image.open(image_path)
                r_image     = yolo.detect_image(image)
                if not os.path.exists(dir_save_path):
                    os.makedirs(dir_save_path)
                r_image.save(os.path.join(dir_save_path, img_name))
                
    else:
        raise AssertionError("Please specify the correct mode: 'predict',  or 'dir_predict'.")
