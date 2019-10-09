import os, numpy, PIL
from PIL import Image
pathMain="images"
import cv2
from glob import glob
def average():
    for path in glob(pathMain+"/*/"):
    # print(next(os.walk('.'))[1])
        files = []
        for r, d, f in os.walk(path):
            for file in f:
                if '.jpg' in file:
                    files.append(os.path.join(r, file))

        counter=0
        for f in files:
            print(counter)
            image=cv2.imread(f)
            counter+=1
            image=cv2.resize(image,(200,200))
            cv2.imwrite(f,image)

        # path="images/adobe"
        print(path)
        allfiles=os.listdir(path)
        imlist=[filename for filename in allfiles if  filename[-4:] in [".jpg"]]
        w,h=Image.open(path+"/"+imlist[0]).size
        N=len(imlist)
        arr=numpy.zeros((h,w,3),numpy.float)
        for im in imlist:
            print(im)
            # print(path+"/"+im)
            imarr=numpy.array(Image.open(path+im),dtype=numpy.float)
            arr=arr+imarr/N
        arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)
        out=Image.fromarray(arr,mode="RGB")
        
        out.save("Average"+path.split('/')[1]+".png")