import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
def createMask():
    paths=os.listdir(".")
    for path in paths:
        if("Average" in path and ".png" in path):
            image_bgr = cv2.imread(path)
            image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
            rectangle = (30, 78, 166, 120)
            mask = np.zeros(image_rgb.shape[:2], np.uint8)
            bgdModel = np.zeros((1, 65), np.float64)
            fgdModel = np.zeros((1, 65), np.float64)
            cv2.grabCut(image_rgb, mask, rectangle,bgdModel,fgdModel,5, cv2.GC_INIT_WITH_RECT)
            mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
            image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]
            image_rgb_nobg=cv2.cvtColor(image_rgb_nobg,cv2.COLOR_RGB2GRAY)
            cv2.imwrite(path.split('.')[0]+"mask.png",image_rgb_nobg)
            image_rgb_nobg=cv2.imread(path.split('.')[0]+"mask.png",0)
            for i in range(len(image_rgb_nobg)):
                for j in range(len(image_rgb_nobg[i])):
                    if(image_rgb_nobg[i][j]>0): image_rgb_nobg[i][j]=255
            cv2.imwrite(path.split('.')[0]+"mask.png",image_rgb_nobg)