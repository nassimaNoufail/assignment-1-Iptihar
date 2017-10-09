from __future__ import division
import cv2
import numpy as np
import math as m


class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        size = np.shape(image)
        newW = int(float(size[0]) * float(fx))
        newH = int(float(size[1]) * float(fy))
        output = np.zeros((newW, newH), np.uint8)
        for row in range(0, newW-3):
            for col in range(0, newH-3):
                x = int(m.floor(float(row)/float(fx)))
                y = int(m.floor(float(col)/float(fy)))
                # for k in range(0, 3):
                output[row+1, col+1] = image[x+1, y+1]

        cv2.imshow('Nearest Neighbor Image', output)
        cv2.waitKey(0)
        return output


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        size = np.shape(image)
        newW = int(float(size[0]) * float(fx))
        newH = int(float(size[1]) * float(fy))
        output = np.zeros((newW, newH), np.uint8)
        for row in range(0, newW ):
            x1 = int(m.floor(float(row)/float(fx)))
            x2 = int(m.ceil(float(row)/float(fx)))
            if x1 == 0:
                x1 = 1
            x = np.remainder(float(row)/float(fx), 1)
            for col in range(0, newH):
                y1 = int(m.floor(float(col)/float(fy)))
                y2 = int(m.ceil(float(col)/float(fy)))
                if y1 == 0:
                    y1 = 1
                img_1 = image[x1, y1]
                img_2 = image[x2, y1]
                img_3 = image[x1, y2]
                img_4 = image[x2, y2]
                y = np.remainder(float(col)/float(fy), 1)
                tr = (img_3 * y) + (img_1 * (1-y))
                br = (img_4 * y) + (img_2 * (1-y))
                output[row, col] = (br*x) + (tr*(1-x))

        newOutput = output.astype(np.uint8)
        cv2.imshow('Bi-Linear Image', newOutput)
        cv2.waitKey(0)
        return newOutput

