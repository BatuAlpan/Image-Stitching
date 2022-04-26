# Image-Stitching

**This is a project made for EE 475: Introduction to Image Processing course in Boğaziçi University EE Department.** 

Image stitching is the operation of combining photos taken from the same panorama. This can be dones by using the classical approach or using the parameters from a convolutional neural network. The  classical approach consists of 4 main steps:

1- [Detecting Keypoints](#detecting-keypoints) <br />
2- [Matching Keypoints](#matching-keypoints) <br />
3- [Computing the Homography Matrix](#computing-the-homography-matrix) <br />
4- [Warping and Blending the Images](#warping-and-blending-the-images) <br />

## Detecting Keypoints

The first step of image stitching is detecting the keypoints/features. This is usually done by using the **SIFT (scale-invariant feature transformation)** algorithm. This algorithm uses Gaussian blurred versions of the image and difference of Gaussians (DoG) technique to highlight the keypoints. Keypoint orientation is found by finding the dominant gradient direction. Finally, rotations and scales of the keypoint are set to a constant so that it can be matched.

As in edge detection, blobs (features) are found by making use of Difference of Gaussians (DoG). Gaussian pyramid is created by applying blur with different sigma values. The higher the sigma the higher the scale of the blob.


## Matching Keypoints

## Computing the Homography Matrix

## Warping and Blending the Images 

Batu ALPAN <br />
Deniz Altay AVCI
