1. Resampling:
    a) in Nearest_neighbor algorithm i used nested for loops to find out every ratio of pixels in original
        image and pasted in new scaled image, i used newRange-3  in loops otherwise get and error said index
        out of range. output images are in output/resize folders.
    b) in bilinear interpolation most important part is to find out 2D coordinate of scaled image and then
        calculate the pixel value according to the ratio. for convenience i used the mathematical ceiling and
        floor function to calculate the coordiante.
2. Region Counting:
    a) compute the histogram is relativly easy, just need to access every pixel with nested loop then calculate
        the sum. to find the optimum threshold, we need to find the weight of background + foreground respectively,
        then find the mean of them. to binarize the image, we need to find histogram and threshold first, then
        calling the same function inside class with "self",we can calculate easily by pixel value bigger than threshold.
    b) for blob coloring i used the algorithm that explained in class which is pretty straight forward, to each pixel,
        check if its neighbor has same value, then return the regions that includes list of pixels.
    c) to compute the pixel value, get x, y coordinate of those pixel in regions, then get the centroid by diving by area,
        but for mark those area, i have to use cv2 library functions to make it happen. somehow the marks are relatively
        small, but they are there. 
