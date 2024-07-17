# K MEANS CLUSTERING:
 
The goal of K means clustering is to partition the dataset into some K clusters, where K is given.  A cluster comprises a group of data points whose inter-point distances are small compared with the distances to points outside of the cluster.

* Methodology:
The method of K means is assigning data points such that the sum of squares of the distances of each data point to its closest vector µ<sub>k</sub> is a minimum.  For each data point there is a corresponding set of binary indicator variables r<sub>nk</sub>  as the 1-of-K coding scheme.
 
Convergence is reached using an iterative procedure in which each iteration involves two successive steps corresponding to successive optimizations with respect to the r<sub>nk</sub> and the µ<sub>k</sub>. These two stages correspond respectively to the E (expectation) and M (maximization) steps of the EM algorithm.


## Image segmentation using K means

As an illustration of the application of the K-means algorithm, this project considers the related problems of image segmentation and image compression. The goal of segmentation is to partition an image into regions each of which has a reasonably homogeneous visual appearance. 

* Methodology
Each pixel in an image is a point in a 3-D space comprising the intensities of the RGB channels, and our segmentation algorithm treats each pixel in the image as a separate data point.

The result of running K-means to convergence, is illustrated by re-drawing the image replacing each pixel vector with the {R,G,B} intensity triplet given by the centre µ<sub>k</sub> to which that pixel has been assigned.  We see that for a given value of K, the algorithm is representing the image using a palette of only K colours.

!(/assets/images/Kmeans.jpg)
