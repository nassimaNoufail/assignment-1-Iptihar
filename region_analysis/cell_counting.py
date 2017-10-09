import cv2
import numpy as np

class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()
        k = 0
        (row, col) = image.shape
        for i in range(row):
            for j in range(col):
                if(image[i,j] == 1 and image[i,j-1] == 0 and image[i-1, j] == 0):
                    regions[i, j] = k
                    k += 1
                if (image[i, j] == 1 and image[i, j-1] == 0 and image[i-1, j] == 1):
                    regions[i, j]  = regions[i-1, j]
                if (image[i, j] == 1 and image[i, j-1] == 1 and image[i-1, j] == 0):
                    regions[i, j] = regions[i, j-1]
                if (image[i, j] == 1 and image[i, j-1] == 1 and image[i-1, j] == 1):
                    regions[i, j] = regions[i-1, j]
                    if (regions[i, j-1] != regions[i-1, j] ):
                        regions[i, j-1] = regions[i-1, j]

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        x = 0.0
        y = 0.0
        n = 0.1
        for pixel in region:
            n = n + 1
            x = x + pixel[0]
            y = y + pixel[1]

        x = x / n
        y = y / n
        k = 1
        print("Region: " + str(k) + ", Centroid: (" + str(x) + "," + str(y) + "), Area: " + str(n))

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return n

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        detector = cv2.SimpleBlobDetector_create()
        keypoints = detector.detect(image)
        output = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.namedWindow("marks", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("marks", output)
        cv2.waitKey(0)
        cv2.destroyWindow("marks")
        return output

