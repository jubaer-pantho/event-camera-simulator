import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, glob
import spatial_op
import tif2jpg
import frame_gen
import temporal_op

#use this module in case the images are given in "tif" format
#tif2jpg.tif2jpg_conv("image_data/")


#use this module to extract camera frames from video
#frame_gen.frame_generate("project.avi", "image_data/")


#Please set the 'size' parameter in spatial and temporal folder if you want to resize the dataset images 
spatial_op.spatial_redundancy("image_data/", "spatial_output/", 5, size=8, resize=1, filetype="*.png")
temporal_op.temporal_redundancy("image_data/", "temporal_output/", 5, size=8, resize=1, filetype="*.png")

