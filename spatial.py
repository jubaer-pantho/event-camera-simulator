import cv2
import numpy as np
from matplotlib import pyplot as plt


def edge_feature_point(img, size, th):
    img_edge = cv2.Canny(img , 100, 200)
    height, width = img_edge.shape
    row = height / size
    col = width / size

    non_roi = 0
    for i in range(0, height, size):
        for j in range(0, width, size):
            patch_in= img_edge[i:(i+size), j:(j+size)]
            roi_pixel = 0
            for m in range(size):
                for n in range(size):
                    if (patch_in[m,n] > 150):
                        roi_pixel = roi_pixel + 1

            if(roi_pixel < th):
                non_roi = non_roi + 1
                img[i:(i+size), j:(j+size), :] = 0    

    return img, non_roi


def mean_absolute_dev(img, size, th=0.09):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape
    row = height / size
    col = width / size

    non_roi = 0
    for i in range(0, height, size):
        for j in range(0, width, size):
            patch_in= gray[i:(i+size), j:(j+size)]
            mean_val = np.mean(patch_in)
            mad_val = 0
            for m in range(size):
                for n in range(size):
                    mad_val = abs(patch_in[m,n] - mean_val)

            mad_val = mad_val / (size*size)
            if(mad_val < th):
                non_roi = non_roi + 1
                img[i:(i+size), j:(j+size), :] = 0    

    return img, non_roi
