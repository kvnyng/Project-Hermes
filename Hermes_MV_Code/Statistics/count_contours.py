import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import imutils
import argparse
import heapq
import random as rng
import statistics

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Convert color image into grayscale
    canny = cv2.Canny(gray, 10, 40)
    return canny

def region_of_interest(image): # You can get rid of this!!
    height = image.shape[0]
    width = image.shape[1]
    margin = 500
    polygons = np.array([ # FillPoly takes a polygon, therefore you must make a polygon
        [(0, height), (width, height), (width, height-margin), (0, height-margin)]
        ]) 
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask) # Taking the bitwise & of the two images, essitally getting rid of anything outside of the area of intrest
    return masked_image

def apply_contour(cropped_image, image):
    copy = np.copy(image)
    ret, threshold = cv2.threshold(cropped_image, 127, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
    #contours = max(contours, key=cv2.contourArea)
    sorted_contours = heapq.nlargest(20, contours, key=cv2.contourArea)
    image = cv2.drawContours(image, sorted_contours, -1, (0, 255, 0), 2)
    print(statistics.mean([cv2.contourArea(x) for x in contours]))
    # print([cv2.contourArea(x) for x in contours])
    return contours

# For video
cap = cv2.VideoCapture("test_media\pothole_sample_clips\statistics 00005652.mov")
while(cap.isOpened()):
    _, frame = cap.read() # Getting the current frame
    pothole_image = np.copy(frame) # Make copy to ensure that OG does not get affected 
    canny_image= canny(pothole_image)
    cropped_image = region_of_interest(canny_image)
    global_countors = apply_contour(cropped_image, frame)
    cv2.imshow('result', frame)
    # print(len(global_countors))
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

#Good: 
#   1e-6
#   9e-7

#Bad:
#   5e-7

# Video names:
#   Good: test_media\pothole_sample_clips\statistics 00005652.mov
#   Bad: test_media\pothole_sample_clips\statistics 00006047.mov


#For Bad Video: (8, 35) for canny -> noisey edge detection
#For Bad Video: (10, 40) for less noisey, easy to see holes