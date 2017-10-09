import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        (row, col) = image.shape
        for i in range(row):
            for j in range(col):
                hist[image[i, j]] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 0
        wB = 0
        wF = 0
        sumA = float(0)
        sumB = float(0)
        varMax = float(0)
        for t in range(0, 256):
            sumA += t * hist[t]
        for r in range(0, 256):
            wB += hist[r]
            if(wB == 0):
                continue
            wF = sum(hist) - wB
            if (wF == 0):
                break
            sumB += float((r * hist[r]))
            mB = sumB/ float(wB)
            mF = (sumA - sumB) / float(wF)
            varBetween = float(wB) * float(wF) * (mB - mF) * (mB - mF)
            if (varBetween > varMax):
                varMax = varBetween
                threshold = r

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        (row, col) = image.shape
        for i in range(row):
            for j in range(col):
                if image[i, j] > 127:
                    bin_img[i,j] = 0
                else:
                    bin_img[i, j] = 255

        return bin_img




