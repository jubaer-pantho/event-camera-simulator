import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, glob
import spatial


def spatial_redundancy(dir_src, dir_dest, th, size=8, resize=1, filetype="*.png"):

    flag = 0
    #read all image files from a folder
    filelist = glob.glob(os.path.join(dir_src, filetype))


    for filename in sorted(filelist):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print("processing... ", str(filename))

            temp_img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

            if (resize == 1):
                new_width = 672
                new_height = 224
                dsize = (new_width, new_height)
                img = cv2.resize(temp_img, dsize, interpolation = cv2.INTER_AREA)
            else:
                img = temp_img

            height, width, depth = img.shape
            row = height / size
            col = width / size

            #img_out, non_roi = spatial.edge_feature_point(img, size, th)
            img_out, non_roi = spatial.mean_absolute_dev(img, size)

            pathName = str(filename)
            outputFile = pathName[len(dir_src):]

            cv2.imwrite(os.path.join(dir_dest, outputFile), img_out)
            non_roi_percentage = (non_roi/(row*col)) * 100

            print("redundancy percentage: ", non_roi_percentage)

