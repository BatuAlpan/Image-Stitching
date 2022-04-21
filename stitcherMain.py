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
keypointThr = 100
distanceThr = 250

image1 = cv.imread(r"example6\example6-1.jpeg")
image1 = cv.cvtColor(image1, cv.COLOR_BGR2RGB)
image2 = cv.imread(r"example6\example6-2.jpeg")
image2 = cv.cvtColor(image2, cv.COLOR_BGR2RGB)
image3 = cv.imread(r"example6\example6-3.jpeg")
image3 = cv.cvtColor(image3, cv.COLOR_BGR2RGB)
image4 = cv.imread(r"example6\example6-4.jpeg")
image4 = cv.cvtColor(image4, cv.COLOR_BGR2RGB)
image5 = cv.imread(r"example6\example6-5.jpeg")
image5 = cv.cvtColor(image5, cv.COLOR_BGR2RGB)

images = [image1, image2, image3, image4, image5]

stitcher = sis()
output = stitcher.stitchImages(images,ransacTol,keypointThr,distanceThr)

if output is not None:    
    plt.imshow(output)
    plt.show()
    cv.imwrite("Example6Output.jpg", cv.cvtColor(output, cv.COLOR_BGR2RGB)) 