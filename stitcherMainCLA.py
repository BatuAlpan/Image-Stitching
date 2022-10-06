import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import itertools
import timeit
import imutils
from imutils import paths
import argparse
from standardImageStitcher import standardImageStitcher as sis

# add cmd arguments with argparse, arguments: input folder, distance thr, keypoint thr, output folder

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('input_path', metavar='input', type=str, nargs='+',
                    help='input path of the images that are going to be stitched')
parser.add_argument('--distanceThr', metavar='dist', type=int, nargs='?', default=200,
                    help='minimum distance for the keypoint matches to be considered as valid')
parser.add_argument('--keypointThr', metavar='keypoint', type=int, nargs='?', default=100,
                    help='minimum # of keypoints for the stitching operation to proceed')

args = parser.parse_args()

print(args.distanceThr)

# Hyperparameters
# ransacTol = 5.0
# distanceThr = 200  # Only considers the keypoint matches lower than this distance.
# keypointThr = 100  # Number of minimum valid keypoints needed to stitch the images.
#
# folderName = "example7"
# numberOfImages = 5
#
# images = []
# for i in range(numberOfImages):
#     image = cv.imread("examples" + "/" + folderName + "/" + folderName + "-" + str(i + 1) + ".jpg")
#     images.append(cv.cvtColor(image, cv.COLOR_BGR2RGB))
#
# stitcher = sis()
# output = stitcher.stitchImages(images, ransacTol, keypointThr, distanceThr, showSteps=False)
#
# if output is not None:
#     # plt.imshow(output)
#     # plt.show()
#     cv.imwrite("results/" + folderName + "_output.jpg", cv.cvtColor(output, cv.COLOR_BGR2RGB))
