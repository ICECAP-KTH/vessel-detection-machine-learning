from posixpath import split
import cv2
from matplotlib.colors import Normalize
import numpy as np
import matplotlib.pyplot as plt
from os.path import join
import os
import tifffile as tiff
import glob

'''
This file create the nir-g-b images from the tiff file.


call crop.py later
'''

CHANNEL =1


#root is a directory, in which tiff files are to be preprocessed.
root='/home/zyh/KTH/ICECAP/DataSet/test_dataset/Dataset/Winter'



# save directory.
NIRgb_dir ='/home/zyh/KTH/ICECAP/DataSet/test_dataset/Dataset/winter_nirgb' 

def plot(img):
    plt.imshow(img)
    plt.show()

def read_tif(name):
    tif_path=join(root,name)
    print(tif_path)
    img=tiff.imread(tif_path)

    

    return img



num = 0
#for area_number in area_list:
    
    
file_list = []
file_list = glob.glob(join(root,'*.tif'))
print(file_list)
for e in file_list:
    img=read_tif(e)
    
    
    norm_3 = cv2.normalize(img[:,:,3], dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    norm_2 = cv2.normalize(img[:,:,2], dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    norm_1 = cv2.normalize(img[:,:,1], dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    norm_0 = cv2.normalize(img[:,:,0], dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    
    
    

    

    NIRgb_img = cv2.merge([norm_3,norm_1,norm_2])
    

    
    
    a=cv2.imwrite(join(NIRgb_dir,str(num)+'.jpg'),NIRgb_img)
    
    num+=1
    
    
        
    






