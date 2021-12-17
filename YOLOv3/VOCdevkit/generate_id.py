import os 
from os.path import join

path ='/home/zyh/KTH/ICECAP/YOLOV4-pytorch/yolov4-pytorch/VOCdevkit/VOC2007/JPEGImages'
img_list=os.listdir(path)
for e in img_list:
    tmp=[]
    tmp=e.strip().split('.')
    f=open('train.txt','a')
    f.write(tmp[0])
    f.write('\n')