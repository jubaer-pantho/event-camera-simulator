import cv2
import numpy as np
from matplotlib import pyplot as plt

import os, glob

def temporal_redundancy(dir_src, dir_dest, th, size =8, resize=1, filetype="*.png"):

    flag = 0
    #read all image files from a folder
    unsortedList = glob.glob(os.path.join(dir_src, filetype))
    filelist = sorted(unsortedList)

    for i in range(1,len(filelist)):
        pathName=str(filelist[i])
        print("processing... ", str(filelist[i]))

        temp_img1 = cv2.imread(filelist[i], cv2.IMREAD_UNCHANGED)

        if (resize == 1):
            new_width = 672
            new_height = 224
            dsize = (new_width, new_height)
            img1 = cv2.resize(temp_img1, dsize, interpolation = cv2.INTER_AREA)
        else:
            img1 = temp_img1


        height, width, depth = img1.shape
        row = height / size
        col = width / size

        temp_img2 = cv2.imread(filelist[i-1], cv2.IMREAD_UNCHANGED)

        if (resize == 1):
            new_width = 672
            new_height = 224
            dsize = (new_width, new_height)
            img2 = cv2.resize(temp_img2, dsize, interpolation = cv2.INTER_AREA)
        else:
            img2 = temp_img2

        nonroi = 0
        for i in range(0, height, size):
            for j in range(0, width, size):
                patch_in= img1[i:(i+size), j:(j+size),:]
                patch_old= img2[i:(i+size), j:(j+size),:]

                roi_pixel = 0
                for m in range(size):
                    for n in range(size):
                        if (abs(int(patch_in[m,n,1]) - int(patch_old[m,n,1])) > 8):
                            roi_pixel = roi_pixel + 1

                if(roi_pixel < th):
                    nonroi = nonroi + 1
                    img1[i:(i+size), j:(j+size),:] = 0

        outputFile = pathName[len(dir_src):]
        cv2.imwrite(os.path.join(dir_dest, outputFile), img1)
        nonroi_rate = (nonroi / (row*col)) * 100
        print(nonroi_rate)



