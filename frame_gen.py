import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, glob


def frame_generate(src_file, dst):
    cap= cv2.VideoCapture(src_file)
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break

        filename = dst + "img"
        cv2.imwrite(filename+str(i)+'.jpg',frame)
        i+=1
 
    cap.release()
    cv2.destroyAllWindows()
