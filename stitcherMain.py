import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import itertools
import timeit
import imutils
from imutils import paths
import argparse
from standardImageStitcher import standardImageStitcher as sis

#Hyperparameters
ransacTol = 5.0
distanceThr = 200 #Only considers the keypoint matches lower than this distance.
keypointThr = 100 #Number of minimum valid keypoints needed to stitch the images. 
 
folderName = "example6"
numberOfImages = 5

images = []
for i in range(numberOfImages):
    image = cv.imread(folderName+"\\"+folderName+"-"+str(i+1)+".jpg")
    images.append(cv.cvtColor(image, cv.COLOR_BGR2RGB))

stitcher = sis()
output = stitcher.stitchImages(images,ransacTol,keypointThr,distanceThr, showSteps=False)

if output is not None:    
    plt.imshow(output)
    plt.show()
    cv.imwrite("Results\\"+folderName+"_output.jpg", cv.cvtColor(output, cv.COLOR_BGR2RGB)) 