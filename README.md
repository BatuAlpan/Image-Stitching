# Image-Stitching

**This is a project made for EE 475: Introduction to Image Processing course in Boğaziçi University EE Department.** 

Image stitching is the operation of combining photos taken from the same panorama. This can be done by using the classical approach or the parameters from a convolutional neural network. The  classical approach consists of 4 main steps:

1- [Detecting Keypoints](#detecting-keypoints) <br />
2- [Matching Keypoints](#matching-keypoints) <br />
3- [Computing the Homography Matrix](#computing-the-homography-matrix) <br />
4- [Warping and Blending the Images](#warping-and-blending-the-images) <br />

## Detecting Keypoints

  The first step of image stitching is detecting the keypoints/features. This is usually done by using the **SIFT (scale-invariant feature transformation)** algorithm. SIFT algorithm uses the Gaussian blurred versions of the image and difference of Gaussians (DoG) technique to highlight the keypoints. 
  
  Gaussian blur is the operation of blurring an image by using the Gaussian distribution as the matrix of filter. As the sigma value (standard deviation) gets higher the Gaussian function gets more spread out further blurring the image. The strong features on the image gets less effected by this filter. Difference of Gaussians (DoG) is a technique for feature enhancement where the Gaussian blurred versions of the image are subtracted from each other. In SIFT algorithm, first a Gaussian pyramid is formed which consists of Gaussian blurred versions of the image with different sigma values. Then the adjacent images are subtracted from each other creating a DoG pyramid. The lower layers of the pyramid correspond to a subtraction between small sigma values and the higher layers correspond to a subtraction between high sigma values. The keypoint candidates are then found by finding the local extrema inside a 3x3x3 grid on the DoG pyramid. Some of these candidates are eliminated by using a threshold and the resulting pixels are the keypoints. An extrema on the higher DoG layer will be a stronger feature therefore it will be a bigger blob and have a higher magnitude compared to the local extrema on the lower layers.   
  
  Orientation of the keypoints are then found by finding the gradients accross a grid inside the blog. The most recurrent direction inside the grid is the dominant gradient direction of the keypoint. Finally, scales and orientations of the keypoints are set to a constant value so that the points become scale-invariant which will be pretty helpful in comparing and matching the images. 

![alt text]([http://url/to/img.png](https://www.researchgate.net/profile/Guohui-Wang-7/publication/256546531/figure/fig1/AS:614316516577318@1523475879934/Diagram-of-SIFT-keypoint-detection-algorithm-showing-one-octave-with-6-Gaussian-image.png))
## Matching Keypoints

## Computing the Homography Matrix

## Warping and Blending the Images 

Batu ALPAN <br />
Deniz Altay AVCI
