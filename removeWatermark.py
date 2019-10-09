import os
import numpy as np
import cv2
# import argparse
from PIL import Image

def check_image_with_pil(path):
    try:
        Image.open(path)
    except Exception as e:
        return False
    return True

def remove(imgPath,output,maskPath,preview):
    if(check_image_with_pil(imgPath)):
        img = cv2.imread(imgPath)
        size=[len(img[0]),len(img)]

        mask = cv2.imread(maskPath,0)
        mask=cv2.resize(mask,tuple(size))
        
        dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

        if(os.path.exists(output)):
            output=output.replace('.png','newVersion.png')

        cv2.imwrite(output,dst)
        if(preview):
            numpy_horizontal_concat = np.concatenate((cv2.imread(imgPath), cv2.imread(output)), axis=1)
            cv2.imshow(imgPath, numpy_horizontal_concat)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("Image with path {} is either not in the right format or is corrupted. ".format(imgPath))

def main():
    path=input("Enter path of file or directory: ")
    outputDir=input("\nEnter output directory or type . to chose the same directory: ")
    if(outputDir=="."):
        if(os.path.isdir(path)): 
            outputDir=path
        else: 
            outputDir=path[::-1].split('/',1)[1][::-1]
    # print(outputDir)
    typeWater=int(input("""
1) Type 1 for adobe stock
2) Type 2 for canstock
3) Type 3 for fotolia
"""))
    if(typeWater==1):
        maskPath="Averageadobemask.png"
    elif(typeWater==2):
        maskPath="Averagecanstockmask.png"
    else:
        maskPath="Averagefotoliamask.png"

    preview=input("\nWould you like to preview the results? (y/n): ")
    if(preview.lower()=='y'):
        previewBool=True
    else:
        previewBool=False

    if(os.path.isdir(path)):
        paths=os.listdir(path)
        counter=0
        for i in  paths:
            if(check_image_with_pil(path+"/"+i)):
                remove(path+"/"+i,outputDir+"/edited"+(i.split('.')[0])+'.png',maskPath,previewBool)
                counter+=1

    else:
        img = cv2.imread(path)
        remove(path,outputDir+"/"+(path.split('/')[len(path.split('/'))-1].split('.')[0])+"Edited.png",maskPath,previewBool)

if(__name__=="__main__"):
    main()
    cv2.destroyAllWindows()
    inp=input("Would you like to continue (y/n): ")
    while(inp.lower()=='y'):
        main()
        inp=input("Would you like to continue (y/n): ")