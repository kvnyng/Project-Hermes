import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import imutils
import argparse
import heapq
import random as rng

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Convert color image into grayscale
    canny = cv2.Canny(gray, 100, 0)
    return canny

def region_of_interest(image): # You can get rid of this!!
    height = image.shape[0]
    width = image.shape[1]
    margin = 600
    polygons = np.array([ # FillPoly takes a polygon, therefore you must make a polygon
        [(0, height), (width, height), (width, height-margin), (0, height-margin)]
        ]) 
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask) # Taking the bitwise & of the two images, essitally getting rid of anything outside of the area of intrest
    return masked_image

# def apply_contor(cropped_image, image):
#     ret, threshold = cv2.threshold(cropped_image, 127, 255, 0)
#     contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#     sorted_contours = max(self.contours, key=cv2.contourArea)
#     area = cv2.contourArea(sorted_contours)

#     cv2.drawContours(image, contours, -1, (0, 255, 0), 2) # Draw Contors


def apply_contour(cropped_image, image):
    copy = np.copy(image)
    ret, threshold = cv2.threshold(cropped_image, 127, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
    #contours = max(contours, key=cv2.contourArea)
    sorted_contours = heapq.nlargest(5, contours, key=cv2.contourArea)
    image = cv2.drawContours(image, sorted_contours, -1, (0, 255, 0), 2)
    return contours

## Bounding Boxes:
# def apply_contour(cropped_image, image):
#     copy = np.copy(image)
#     ret, threshold = cv2.threshold(cropped_image, 127, 255, 0)
#     contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
#     sorted_contours = heapq.nlargest(10, contours, key=cv2.contourArea)

#     # Approximate contours to polygons + get bounding rects and circles
#     sorted_contours_poly = [None]*len(sorted_contours)
#     boundRect = [None]*len(sorted_contours)
#     centers = [None]*len(sorted_contours)
#     radius = [None]*len(sorted_contours)
#     for i, c in enumerate(sorted_contours):
#         sorted_contours_poly[i] = cv2.approxPolyDP(c, 3, True)
#         boundRect[i] = cv2.boundingRect(sorted_contours_poly[i])
#         centers[i], radius[i] = cv2.minEnclosingCircle(sorted_contours_poly[i])

#     drawing = np.zeros((canny_image.shape[0], canny_image.shape[1], 3), dtype=np.uint8)
#      # Draw polygonal contour + bonding rects + circles
#     for i in range(len(sorted_contours)):
#         color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
#         cv2.drawContours(drawing, sorted_contours_poly, i, color)
#         cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
#           (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
#         #cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)

#     return drawing

# For image:
image =  cv2.imread('test_media\pothole_test.jpg')
copy_image = np.copy(image)
pothole_image = np.copy(image) # Make copy to ensure that OG does not get affected 
canny_image= canny(pothole_image)
cropped_image = region_of_interest(canny_image)
contor_image = apply_contour(cropped_image, copy_image)

cv2.imshow('result', copy_image)
cv2.waitKey(0)

# # For image:
# image =  cv2.imread('test_media\pothole_test.jpg')
# copy_image = np.copy(image)
# pothole_image = np.copy(image) # Make copy to ensure that OG does not get affected 
# canny_image= canny(pothole_image)
# cropped_image = region_of_interest(canny_image)
# boxed_image = apply_contour(cropped_image, copy_image)
# final_image = cv2.addWeighted(image, 0.8, boxed_image, 1, 1) # Overlay the line_image with lane_image
# cv2.imshow('result', final_image)
# cv2.waitKey(0)
# # For video
# cap = cv2.VideoCapture("test_media\pothole_sample_clips\pothole_clip00003444.mp4")
# while(cap.isOpened()):
#     _, frame = cap.read() # Getting the current frame
#     pothole_image = np.copy(frame) # Make copy to ensure that OG does not get affected 
#     canny_image= canny(pothole_image)
#     cropped_image = region_of_interest(canny_image)
#     boxed_image = apply_contour(cropped_image, frame)
#     final_image = cv2.addWeighted(frame, 0.8, boxed_image, 1, 1) # Overlay the line_image with lane_image
#     cv2.imshow('result', final_image)
#     cv2.waitKey(1)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()