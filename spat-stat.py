import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, glob



data = []

def variation_test(patch_in, size=16):
    avg = sum(map(sum, patch_in[:,:]))/ (size*size)

    manhattan_dist = 0
    for m in range(size):
        for n in range(size):
            manhattan_dist += ((avg - patch_in[m,n]) ** 2)


    mad_val = manhattan_dist / (size*size)
    return mad_val




dist_array = []

def spatial_redundancy(dir_src, dir_dest, th = 0, size=16):

    flag = 0
    #read all image files from a folder
    filelist = glob.glob(os.path.join(dir_src, '*.jpg'))


    for filename in sorted(filelist):
        if filename.endswith(".jpg"):
            #print("processing... ", str(filename))

            img = cv2.imread(filename, 0)
            imgOut = cv2.imread(filename, cv2.IMREAD_UNCHANGED)            

            height, width = img.shape

            row = height / size
            col = width / size

            non_roi = 0
            for i in range(0, height, size):
                for j in range(0, width, size):
                    patch_in= img[i:(i+size), j:(j+size)]
                    #print(patch_in.shape)
                    mad_val = variation_test(patch_in, size)


                    if(mad_val <= th):
                        non_roi = non_roi + 1
                        imgOut[i:(i+size), j:(j+size), :] = 255


            pathName = str(filename)
            outputFile = pathName[len(dir_src):]

            cv2.imwrite(os.path.join(dir_dest, outputFile), imgOut)
            non_roi_percentage = (non_roi/(row*col)) * 100
            dist_array.append(non_roi_percentage)

            #print(non_roi_percentage)





spatial_redundancy("images-flit/", "filt-spat/", 1, 16)

#spatial_redundancy("images-reduced/", "red-spat/", 1, 16)

#spatial_redundancy("images-mask/", "mask-spat/", 3000, 16)

#plt.hist(data, bins = 30)


print("Average : ", (sum(dist_array)/ len(dist_array)))

plt.plot(dist_array)
plt.ylabel('Detected Redundancy Percentage')
plt.xlabel('Frames')

plt.show()



