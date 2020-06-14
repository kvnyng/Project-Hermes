import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import imutils
import argparse

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Convert color image into grayscale
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # Using Gaussian Blur to smooth image
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    margin = 100
    polygons = np.array([ # FillPoly takes a polygon, therfore you must make a polygon
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
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    threshold_area_min = 75 # Threshold area 
    threshold_area_max = 200
    for i in range (len(contours)):        
        area = cv2.contourArea(contours[i], False) 
        #specific_contour = contours[i]     
        if threshold_area_min < area < threshold_area_max:                  
            image = cv2.drawContours(image, contours, i, (0, 255, 0), 2)
    

    # print("Number of contors = " + str(len(contours)))
    # print(contours[0])

# image =  cv2.imread('test_media\pothole_test.jpg')
# copy_image = cv2.imread('test_media\pothole_test.jpg')
# pothole_image = np.copy(image) # Make copy to ensure that OG does not get affected 
# canny_image= canny(pothole_image)
# cropped_image = region_of_interest(canny_image)
# contor_image = apply_contour(cropped_image, copy_image)

# cv2.imshow('result', copy_image)
# cv2.waitKey(0)

cap = cv2.VideoCapture("test_media\pothole_test_video.mp4")
while(cap.isOpened()):
    _, frame = cap.read() # Getting the current frame
    pothole_image = np.copy(frame) # Make copy to ensure that OG does not get affected 
    canny_image= canny(pothole_image)
    cropped_image = region_of_interest(canny_image)
    contour_image = apply_contour(cropped_image, frame)
    cv2.imshow('result', frame)
    cv2.waitKey(10)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()