import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import itertools
import timeit
import imutils
from imutils import paths
import argparse

class standardImageStitcher:
    pass
    
    #Finds the maximum of the edge points for bordering
    def findEdgeLoc(self,matrix,image):
        length, width = np.size(image,0), np.size(image,1)
        edges = np.array([[0,0,1],[width,0,1],[0,length,1],[width,length,1]])
        max_x, max_y = 0, 0
        for loc in edges:
            newLoc = matrix.dot(loc)
            newLoc = newLoc / newLoc[2]
            max_x, max_y = max(max_x, newLoc[0]), max(max_y, newLoc[1])
        return int(max_x), int(max_y)

    def stitchImages(self,images,ransacTol,keypointThr,distanceThr,showSteps=False):
        output = images[0]
        start = timeit.default_timer()
        for i in range(len(images)-1):
            image1, image2 = output, images[i+1]

            #Keypoints and keypoint descriptors of the input images are found.
            sift = cv.SIFT_create()
            keypoints1, des1 = sift.detectAndCompute(image1, None)
            image1key = cv.drawKeypoints(image1, keypoints1, None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            print(f"Number of keypoints for image 1: {len(keypoints1)}")
            keypoints2, des2 = sift.detectAndCompute(image2, None)
            image2key = cv.drawKeypoints(image2, keypoints2, None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            print(f"Number of keypoints for image 2: {len(keypoints2)}")

            #Keypoints are matched
            bf = cv.BFMatcher(cv.NORM_L2, crossCheck = True) #Brute force matching using L2 norm
            matches = bf.match(des1, des2)
            matches = sorted(matches, key = lambda x: x.distance)
            imMatches = cv.drawMatches(image1, keypoints1, image2, keypoints2, matches[1:20], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

            print(f"Number of matches: {len(matches)}")

            #Homography matrix is found if the images can be stitched
            points1, points2, flag = np.array([]), np.array([]), 0
            #Thresholding is done to eliminate non-maching images
            impKey = [matches[i].distance for i in range(len(matches)) if matches[i].distance < distanceThr] 

            if len(impKey) < keypointThr:
                flag = 1

            if flag == 0:
                for i in range(len(matches)):
                    if matches[i].distance > distanceThr: #Points above a certain threshold are ignored to make the code faster. 
                        continue
                    #Indices of the matches are found and then the keypoints and their coordinates (.pt) are found. 
                    points1 = np.append(points1, keypoints1[matches[i].queryIdx].pt) 
                    points2 = np.append(points2, keypoints2[matches[i].trainIdx].pt)

                points1 = points1.reshape(-1,1,2)
                points2 = points2.reshape(-1,1,2)

                homograhyMat, mask = cv.findHomography(points1, points2, cv.RANSAC, ransacTol)
            elif flag == 1:
                print("Images cannot be stitched.")
                return None
                
            #Stitching is done by using warping
            homograhyMatInv = np.linalg.inv(homograhyMat)
            max_x, max_y = self.findEdgeLoc(homograhyMatInv,image2)
            im1_x, im1_y = np.size(image1,1), np.size(image1,0)
            output = cv.warpPerspective(image2,homograhyMat,(max(max_x,im1_x),max(max_y,im1_y)),dst=output,
            flags=cv.WARP_INVERSE_MAP, borderValue=cv.BORDER_CONSTANT) #Image 2 is warped with homography matrix.

            #Images are added by throwing away the black gaps 
            img1Gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
            ret, mask = cv.threshold(img1Gray, 1, 255, cv.THRESH_BINARY)
            mask_inv = cv.bitwise_not(mask)
            roi = output[0:image1.shape[0], 0:image1.shape[1]]

            output_img1 = cv.bitwise_and(roi,roi,mask = mask_inv) #Black-out the regions of img1 on the warped image.
            img1 = cv.bitwise_and(image1,image1,mask = mask)

            dst = cv.add(img1,output_img1)
            output[0:image1.shape[0], 0:image1.shape[1]] = dst

            if showSteps == True:
                cv.imshow("Image 1 Keypoints", image1key)
                #cv.imwrite("image1key.jpg", image1key)
                cv.imshow("Image 2 Keypoints", image2key)
                #cv.imwrite("image2key.jpg", image2key)
                cv.waitKey(0)

                plt.imshow(imMatches)
                #cv.imwrite("Matches.jpg", imMatches)
                plt.show()

                plt.imshow(output)
                plt.show()

        stop = timeit.default_timer()
        print(f'Time: {(stop - start):.3f} sec.') 
        return output

def main():
    #Hyperparameters
    ransacTol = 5.0
    keypointThr = 10
    distanceThr = 500

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

    stitcher = standardImageStitcher()
    stitcher.stitchImages(images,ransacTol,keypointThr,distanceThr)

if __name__ == '__main__':
    main()
    