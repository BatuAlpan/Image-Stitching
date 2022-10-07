import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import itertools
import timeit
import imutils
from imutils import paths
import argparse
import glob
from standardImageStitcher import standardImageStitcher as sis

# add cmd arguments with argparse, arguments: input folder, distance thr, keypoint thr, output folder

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('input_path', metavar='input', type=str, nargs='+',
                    help='Input path of the images that are going to be stitched')
parser.add_argument('--distanceThr', metavar='dist', type=int, nargs='?', default=200,
                    help='Minimum distance for the keypoint matches to be considered as valid')
parser.add_argument('--keypointThr', metavar='keypoint', type=int, nargs='?', default=100,
                    help='Number of minimum valid keypoints needed to stitch the images')
parser.add_argument('output_path', metavar='output', type=str, nargs='+',
                    help='Output path of the stitched image')
parser.add_argument('output_name', metavar='name', type=str, nargs='+',
                    help='Name of the stitched image')

args = parser.parse_args()

inputFolder = args.input_path[0]
ransacTol = 5.0
distanceThr = args.distanceThr  # Only considers the keypoint matches lower than this distance.
keypointThr = args.keypointThr  # Number of minimum valid keypoints needed to stitch the images.

images = []
imagePaths = glob.glob(inputFolder + '/*')
imagePaths.sort()
for i in range(len(imagePaths)):
    image = cv.imread(imagePaths[i])
    images.append(cv.cvtColor(image, cv.COLOR_BGR2RGB))

stitcher = sis()
output = stitcher.stitchImages(images, ransacTol, keypointThr, distanceThr, showSteps=False)

if output is not None:
    # plt.imshow(output)
    # plt.show()
    cv.imwrite(args.output_path[0] + "/" + args.output_name[0] + ".jpg", cv.cvtColor(output, cv.COLOR_BGR2RGB))
