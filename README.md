# Image-Stitching

**This is a project made for EE 475: Introduction to Image Processing course in Boğaziçi University EE Department.** 

Image stitching is the operation of combining photos taken from the same panorama. This can be done by using the classical approach or the parameters from a convolutional neural network. The  classical approach consists of 4 main steps:

1- [Detecting Keypoints](#detecting-keypoints) <br />
2- [Matching Keypoints](#matching-keypoints) <br />
3- [Computing the Homography Matrix](#computing-the-homography-matrix) <br />
4- [Warping and Blending the Images](#warping-and-blending-the-images) <br />

## Detecting Keypoints

  The first step of image stitching is detecting the keypoints/features. This is usually done by using the **SIFT (scale-invariant feature transformation)** algorithm. SIFT algorithm uses the Gaussian blurred versions of the image and difference of Gaussians (DoG) technique to highlight the keypoints. 
  
  Gaussian blur is the operation of blurring an image by using the Gaussian distribution as the kernel of filter. As the sigma value (standard deviation) gets higher the Gaussian function gets more spread out further blurring the image. The strong features on the image get less effected by this filter. Difference of Gaussians (DoG) is a technique for feature enhancement where the Gaussian blurred versions of the image are subtracted from each other. 
  
  In SIFT algorithm, first a Gaussian pyramid is formed which consists of Gaussian blurred versions of the image with different sigma values. Then the adjacent blurred images are subtracted from each other creating a DoG pyramid. The lower layers of the pyramid correspond to a subtraction between small sigma values and the higher layers correspond to a subtraction between large sigma values. The keypoint candidates are then found by finding the local extrema inside a 3x3x3 grid on the DoG pyramid. Some of these candidates are eliminated by using a threshold and the resulting pixels are the keypoints. An extrema on a higher DoG layer will be a stronger feature therefore it will be a bigger blob and have a higher magnitude compared to the local extrema on the lower layers.   
  
  Orientation of the keypoints are then found by finding the gradients accross a grid inside the blog. The most recurrent direction inside the grid is the dominant gradient direction of the keypoint. Finally, scales and orientations of the keypoints are set to a constant value so that the points become scale-invariant which will be pretty helpful in comparing and matching the images. 

![Find the keypoints](https://www.researchgate.net/publication/342148975/figure/fig1/AS:901943815847936@1592051571533/SIFT-Algorithm-steps.jpg)
## Matching Keypoints

  The keypoints are matched by using a principle called keypoint descriptors. Each detected keypoint has its own descriptor based on its gradient accross the grid inside the blob. To find the descriptor, first the blob is divided into 4 quadrants. Then a histogram of the gradient directions are created for each of the quadrants. This histogram is the keypoint descriptor.
  
  Keypoints are matched by looking at the histogram distance between two keypoint. There are a variety of metrics to measure the distance between the keypoints such as L2 distance, intersection, Bhattacharyya distance, correlation etc. To make the calculations easier L2 distance was used in this project. Sometimes one of the images will have a very distinct keypoint. As a result of that the match of this keypoint will have a very high distance and most probably this will be a wrong match. In order to prevent this we added a distance threshold that only considers the matches under a certain distance value. This correct most of the false matches. The default value is 200 but the user can change this as a command line argument. 
  
![Keypoint descriptor](https://www.i2tutorials.com/wp-content/media/2019/09/SIFT-and-SURF-1-i2tutorials.jpg)

## Computing the Homography Matrix

## Warping and Blending the Images 

Batu ALPAN <br />
Deniz Altay AVCI
