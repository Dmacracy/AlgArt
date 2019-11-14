import os
import sys
import time
import random
import datetime

import cv2
import numpy as np

def create_alg_arts(inDir):
    inFiles = [os.path.join(inDir, f) for f in os.listdir(inDir) if (f.endswith('.jpg') or f.endswith('.jpeg'))]
    for imgName in inFiles:
        for i in range(1, 10):
            #Quantize calls:
            numCols = i
            outputName = os.path.splitext(imgName)[0] + "_" + str(numCols) + "_colors" + os.path.splitext(imgName)[1]
            cv2.imwrite(outputName, color_quantize(imgName, numCols))

        for i in range(30, 180, 30):
            #Hue Rot call:
            deg = i
            outputName = os.path.splitext(imgName)[0] + "_" + str(deg) + "_degrot" + os.path.splitext(imgName)[1]
            cv2.imwrite(outputName, hue_rotate(imgName, deg))

        for i in range(5):
            #Swap Id call:
            swapID = i
            outputName = os.path.splitext(imgName)[0] + "_" + str(swapID) + "_swapped" + os.path.splitext(imgName)[1]
            cv2.imwrite(outputName, swap_chans(imgName, swapID))

def swap_chans(imgName, swapId):
    img = cv2.imread(imgName)
    split = cv2.split(img)
    if swapId == 0:
        img = cv2.merge([split[1], split[2], split[0]])
    elif swapId == 1:
        img = cv2.merge([split[2], split[0], split[1]])
    elif swapId == 2:
        img = cv2.merge([split[1], split[0], split[2]])
    elif swapId == 3:
        img = cv2.merge([split[2], split[1], split[0]])
    elif swapId == 4:
        img = cv2.merge([split[0], split[2], split[1]])
    return img

def hue_rotate(imgName, degrees):
    '''Given an image filename, this function rotates the image 
       by the given number of degrees in the hue plane of 
       opencv's HSV space. It returns the resulting image'''
    img = cv2.imread(imgName)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_cpy = img.copy()
    for y in range(len(img)):
        for x in range(len(img[0])):
            img_cpy[y, x, 0] = (int(img_cpy[y, x, 0]) + int(degrees)) % 180
    return cv2.cvtColor(img_cpy, cv2.COLOR_HSV2BGR)
    


def color_quantize(imgName, numCols):
    '''Given an image filename, this function runs k-clustering on the image's 
       colors with k=numCols clusters and then sets ever pixel in a given cluster 
       to the centroid color vector of the cluster. It then returns the color quantied image.'''
    img = cv2.imread(imgName)
    # Reshape the image matrix to a lst of each idivid pixel 
    Z = img.reshape((-1, 3))
    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = numCols
    ret,label,center=cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return res2

if __name__ == "__main__":
    inDir = sys.argv[1]
    create_alg_arts(inDir)
    
    # Quantize call:
    #numCols = int(sys.argv[2])
    #outputName = os.path.splitext(imgName)[0] + "_" + sys.argv[2] + "_colors" + os.path.splitext(imgName)[1]
    #cv2.imwrite(outputName, color_quantize(imgName, numCols))
    
    # Hue Rot call:
    #deg = int(sys.argv[2])
    #outputName = os.path.splitext(imgName)[0] + "_" + sys.argv[2] + "_degrot" + os.path.splitext(imgName)[1]
    #cv2.imwrite(outputName, hue_rotate(imgName, deg))

    # Swap Id call:
    #swapID = int(sys.argv[2]) % 5
    #outputName = os.path.splitext(imgName)[0] + "_" + sys.argv[2] + "_swapped" + os.path.splitext(imgName)[1]
    #cv2.imwrite(outputName, swap_chans(imgName, swapID))
    
