import os 
from os.path import join
import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
'''
This file crop the 512 by 512 images from 1000 by 1000 images,
please firstly call createNIR_G_B.py, then, call this file
'''

SAVE_MODE = 1

""" root='../'
if SAVE_MODE ==1:
    f = open('./test.txt','w') """






#image_dir is the dictory of NIR-G-B images, 
#the save root is the image_dir/crop
image_dir='/home/zyh/ICECAP/DataSet/test_dataset/Dataset/winter_nirgb'
save_root=join(image_dir,'crop')


IMAGE_SIZE=512
STEP=450 #400,20
list1=glob.glob(join(image_dir,'*.jpg'))


for image_path in list1:

    image=cv2.imread(image_path)
    image_number = image_path.strip().split('/')[-1]
    print(image_number) 
    
 


    w=image.shape[1]
    h=image.shape[0]
    c=image.shape[2]

    
    for j in range(int(h/STEP)):
        for i in range( int(w/STEP)):
            
            x_crop=min(STEP*i+IMAGE_SIZE,w)
            y_crop=min(STEP*j+IMAGE_SIZE,h)

            x_start=STEP*i
            y_start=STEP*j

            sub_image=np.zeros((IMAGE_SIZE,IMAGE_SIZE,c),dtype=np.uint8)
            
            
            sub_image[0:(y_crop-y_start)  , 0 : (x_crop-x_start) ,:]=image[y_start:y_crop,x_start:x_crop,:]
            if x_crop == w:
                sub_image[:,(x_crop-x_start):,:]=0
            if y_crop == h:
                sub_image[(y_crop-y_start):,:,:]=0

                
            
           
            if SAVE_MODE ==1:
            
                """ if not os.path.exists(join(save_root,save_dir)):
                    os.mkdir(join(save_root,save_dir)) """

                #sub_image = sub_image.astype('numpy.uint8')
                
                a=cv2.imwrite(join(save_root,image_number+str(i)+'_'+str(j)+'.jpg')  ,sub_image)
                print(a)
                #f.write(join(save_root,save_dir,str(i)+'_'+str(j)+'.jpg'))
                #f.write('\n')
            
            else:

            
                plt.imshow(sub_image)
                plt.show()
                #a=cv2.imwrite(('./'+str(i)+'_'+str(j)+'.jpeg')  ,sub_image)
    
                

   
