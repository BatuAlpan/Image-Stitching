# Image-Stitching

**This is a project made for EE 475: Introduction to Image Processing course in Boğaziçi University EE Department.** 

Image stitching is the operation of combining photos taken from the same panorama. This can be done by using the classical approach or the parameters from a convolutional neural network. The  classical approach consists of 4 main steps:

1- [Detecting Keypoints](#detecting-keypoints) <br />
2- [Matching Keypoints](#matching-keypoints) <br />
3- [Computing the Homography Matrix](#computing-the-homography-matrix) <br />
4- [Warping and Blending the Images](#warping-and-blending-the-images) <br />

## Detecting Keypoints

The first step of image stitching is detecting the keypoints/features. This is usually done by using the **SIFT (scale-invariant feature transformation)** algorithm. SIFT algorithm uses Gaussian blurred versions of the image and difference of Gaussians (DoG) technique to highlight the keypoints. The higher the sigma value of the Gaussian blur filter the higher the scale of the blob. Orientation of the keypoints are then found by finding the dominant gradient direction. Finally, scales and orientations of the keypoints are set to a constant value so that the points become scale-invariant. One great advantage of this operation is creating a huge ease in the keypoint matching operation which will be further discussed in the upcoming section. 


## Matching Keypoints

## Computing the Homography Matrix

## Warping and Blending the Images 

Batu ALPAN <br />
Deniz Altay AVCI
