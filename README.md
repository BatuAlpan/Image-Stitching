# Image-Stitching

**This is a project made for EE 475: Introduction to Image Processing course in Boğaziçi University EE Department.** 

Image stitching is the operation of combining photos taken from the same panorama. This can be done by using the classical approach or the parameters from a convolutional neural network. The  classical approach consists of 4 main steps:

1- [Detecting Keypoints](#detecting-keypoints) <br />
2- [Matching Keypoints](#matching-keypoints) <br />
3- [Computing the Homography Matrix](#computing-the-homography-matrix) <br />
4- [Warping and Blending the Images](#warping-and-blending-the-images) <br />

## Detecting Keypoints

/t The first step of image stitching is detecting the keypoints/features. This is usually done by using the **SIFT (scale-invariant feature transformation)** algorithm. SIFT algorithm uses the Gaussian blurred versions of the image and difference of Gaussians (DoG) technique to highlight the keypoints. 
  
  Gaussian blur is the operation of blurring an image by using the Gaussian distribution as the matrix of filter. As the sigma value (standard deviation) gets higher the Gaussian function gets more spread out further blurring the image. The strong features on the image gets less effected by this filter. Difference of Gaussians (DoG) is a technique for feature enhancement where the Gaussian blurred versions of the image are subtracted from each other. In SIFT algorithm, first a Gaussian pyramid is formed which consists of Gaussian blurred versions of the image with different sigma values. Then the adjacent images are subtracted from each other creating a DoG pyramid. The lower layers of the pyramid correspond to a subtraction between small sigma values and the higher layers correspond to a subtraction between high sigma values. The keypoint candidates are then found by finding the local extrema inside a 3x3x3 grid on the DoG pyramid. Some of these candidates are eliminated by using a threshold and the resulting pixels are the keypoints. An extrema on the higher DoG layer will be a stronger feature therefore it will be a bigger blob and have a higher magnitude compared to the local extrema on the lower layers.   
  
  Orientation of the keypoints are then found by finding the dominant gradient direction. Finally, scales and orientations of the keypoints are set to a constant value so that the points become scale-invariant. One great advantage of this operation is creating a huge ease in the keypoint matching operation which will be further discussed in the upcoming section. 


## Matching Keypoints

## Computing the Homography Matrix

## Warping and Blending the Images 

Batu ALPAN <br />
Deniz Altay AVCI
